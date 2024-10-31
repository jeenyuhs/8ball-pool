import math
import time
import pygame
import pymunk
import pymunk.pygame_util
from objects.cue import Cue
from objects.table import Table
import settings
import utils


def game():
    pygame.init()

    surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("DDU Projekt - 8ball")

    draw_options = pymunk.pygame_util.DrawOptions(surface)

    clock = pygame.time.Clock()
    running = True

    # game variables
    balls_moving = False
    aiming = False
    aiming_base_y = 0

    table = Table()
    table.initialize_balls()

    utils.initialize_slab_collision_detection()

    cue = Cue(pygame.image.load("assets/images/cue.png").convert_alpha(), table.cue_ball.body.position)

    _previous_y_diff = 0

    pockets = (
        [86, 84],
        [798, 61],
        [1512, 83],
        [1512, 809],
        [798, 833],
        [86, 807]
    )
    POCKET_RADIUS = 35
    flip_turns = True

    while running:
        dt = clock.tick(settings.FPS)
        utils.SPACE.step(1 / settings.FPS)

        # standard
        surface.fill(settings.COLORS["WOOD"])

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and not balls_moving:
                    if not aiming:
                        _, y = pygame.mouse.get_pos()
                        aiming_base_y = y

                    aiming = True

                if event.key == pygame.K_d:
                    settings.DEBUG = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL and aiming:
                    aiming = False

                if event.key == pygame.K_d:
                    settings.DEBUG = False

            if event.type == pygame.QUIT:
                running = False

        table.draw(surface)

        any_moving = any(int(ball.body.velocity[0]) != 0 or int(ball.body.velocity[1]) != 0 for ball in table.balls)

        if not any_moving and balls_moving:
            balls_moving = False

            if not table.shooter.has_potted_new_balls:
                table.shooter.is_shooting = False
                table.who_is_waiting.is_shooting = True
            else:
                table.shooter.has_potted_new_balls = False

            # wait one second
            time.sleep(1)

        balls_moving = any_moving

        if not balls_moving:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cue.rect.center = table.cue_ball.body.position

            if not aiming:
                x_dist = table.cue_ball.body.position[0] - mouse_x
                y_dist = -(table.cue_ball.body.position[1] - mouse_y)
                cue.angle = math.degrees(math.atan2(y_dist, x_dist))

            if aiming:
                y_diff = mouse_y - aiming_base_y
                speed = 0
                # the cue is moving towards the balls, and therefore the force 
                # should start to be calculated.
                if _previous_y_diff != 0 and (y_diff - _previous_y_diff) < 0:
                    # min speed = 0.5, max speed = 5
                    speed = min(6, max(0.5, (_previous_y_diff - y_diff) / dt))

                _previous_y_diff = y_diff

                # about the time the cue hits the cue ball
                if y_diff <= -12.0:
                    x_impulse = math.cos(math.radians(cue.angle))
                    y_impulse = math.sin(math.radians(cue.angle))

                    table.cue_ball.body.apply_impulse_at_local_point((2000 * -x_impulse * speed, 2000 * y_impulse * speed), (0, 0))
                else:
                    cue_angle = math.radians(cue.angle)
                    cue.rect.center = (
                        table.cue_ball.body.position[0] + min(130, y_diff) * math.cos(cue_angle), 
                        table.cue_ball.body.position[1] + min(130, y_diff) * -math.sin(cue_angle)
                    )
            
            cue.draw(surface)
        else:
            for ball in table.balls:
                # skip all balls that aren't moving
                if int(ball.body.velocity[0]) == 0 or int(ball.body.velocity[1]) == 0:
                    continue

                for pocket in pockets:
                    dist_to_pocket = math.dist(ball.body.position, pocket)

                    # threshold should be 45% of POCKET_RADIUS
                    if dist_to_pocket <= POCKET_RADIUS * (1 - 0.45):
                        if table.shooter.has_ball_type == None:
                            table.shooter.has_ball_type = ball.type
                            table.shooter.potted_balls.append(ball)
                            table.shooter.has_potted_new_balls = True

                        if table.shooter.has_ball_type != ball.type:
                            table.who_is_waiting.potted_balls.append(ball)
                            table.shooter.is_shooting = False
                            table.who_is_waiting.is_shooting = True

                        table.balls.remove(ball)
                        utils.SPACE.remove(ball.body)

        if settings.DEBUG:
            utils.SPACE.debug_draw(draw_options)

            for pocket in pockets:
                pygame.draw.circle(surface, (255, 0, 0), pocket, POCKET_RADIUS)

        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    game()
