import collections
import math
import pygame
import pymunk
import pymunk.pygame_util
from objects.ball import Ball
from objects.cue import Cue
from objects.table import Table
import settings
import utils


def game():
    pygame.init()

    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("DDU Projekt - 8ball")

    draw_options = pymunk.pygame_util.DrawOptions(screen)
    utils.initialize_slab_collision_detection()

    cue_ball = Ball.create((600, settings.SCREEN_HEIGHT // 2 + 20))
    cue = Cue(pygame.image.load("assets/images/cue.png").convert_alpha(), cue_ball.body.position)

    clock = pygame.time.Clock()
    running = True

    # game variables
    balls_moving = False
    aiming = False
    aiming_base_y = 0

    dt = 0
    
    _previous_y_diff = 0

    while running:
        # standard
        screen.fill(settings.COLORS["WOOD"])

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

        Table.draw(screen)

        balls_moving = cue_ball.body.velocity.length > 0

        if not balls_moving:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cue.rect.center = cue_ball.body.position

            if not aiming:
                x_dist = cue_ball.body.position[0] - mouse_x
                y_dist = -(cue_ball.body.position[1] - mouse_y)
                cue.angle = math.degrees(math.atan2(y_dist, x_dist)) - 180

            if aiming:
                y_diff = mouse_y - aiming_base_y
                speed = 0
                # the cue is moving towards the balls, and therefore the force 
                # should start to be calculated.
                if _previous_y_diff != 0 and (y_diff - _previous_y_diff) < 0:
                    # length = y_diff + (_previous_y_diff + y_diff)
                    # min speed = 0.5, max speed = 6
                    speed = min(6, max(0.5, (_previous_y_diff - y_diff) / dt))

                _previous_y_diff = y_diff

                # about the time the cue hits the cue ball
                if y_diff <= -12.0:
                    x_impulse = math.cos(math.radians(cue.angle))
                    y_impulse = math.sin(math.radians(cue.angle))
                    cue_ball.body.apply_impulse_at_local_point((2000 * -x_impulse * speed, 2000 * y_impulse * speed), (0, 0))
                else:
                    cue_angle = math.radians(cue.angle)
                    cue.rect.center = (
                        cue_ball.body.position[0] + min(130, y_diff) * math.cos(cue_angle), 
                        cue_ball.body.position[1] + min(130, y_diff) * -math.sin(cue_angle)
                    )
            
            cue.draw(screen)

        utils.SPACE.debug_draw(draw_options)

        pygame.display.flip()
        dt = clock.tick(120)
        utils.SPACE.step(1 / 120)

    pygame.quit()


if __name__ == "__main__":
    game()
