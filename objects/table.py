import pygame

from objects.ball import Ball, BallType
from objects.player import Player
import settings
import utils


class Table:
    def __init__(self):
        self.balls: list[Ball] = []
        self.players: list[Player] = []

    @property
    def cue_ball(self) -> Ball:
        return self.balls[-1]
    
    @property
    def shooter(self) -> Player:
        return self.players[0] if self.players[0].is_shooting else self.players[1]
    
    @property
    def who_is_waiting(self) -> Player:
        return self.players[0] if not self.players[0].is_shooting else self.players[1]
    
    def take_turns(self) -> None:
        self.shooter.is_shooting = False
        self.who_is_waiting.is_shooting = True

    def initialize_balls(self) -> None:
        positions = []
        dist = settings.BALL_RADIUS * 2
        for i in range(5):
            for j in range(4):
                x = i * dist
                y = j * dist + i * (dist / 2)
                positions.append((x + 200, y + 200))

        for ball in range(15):
            ball_type = BallType.SOLID
            # 8ball
            if ball + 1 == 8:
                ball_type = BallType.EIGHT_BALL
            # stripe
            if ball + 1 > 8:
                ball_type = BallType.STRIPE

            print(ball + 1)

            ball_obj = Ball.create(positions[ball], ball_type)
            ball_obj.image = pygame.image.load(f"assets/images/balls/ball_{ball + 1}.png").convert_alpha()

            self.balls.append(ball_obj)

        cue_ball = Ball.create(
            (
                settings.SCREEN_WIDTH / 1.5, 
                settings.SCREEN_HEIGHT // 2 + 20
            ), 
            type = BallType.CUE
        )
        cue_ball.image = pygame.image.load(f"assets/images/balls/cue_ball.png").convert_alpha()

        self.balls.append(cue_ball)


    def draw(self, surface: pygame.Surface) -> None:
        table = pygame.image.load("assets/images/table.png").convert_alpha()
        surface.blit(table, (0, 0))

        DEBUG_COLORS = (
            (255, 0, 0),    # red
            (0, 255, 0),    # green
            (0, 0, 255),    # blue
            (255, 255, 0),   # yellow
            (255, 0, 255),   # magenta
            (0, 255, 255),   # idfk
        )

        for positions in utils.SLABS:
            if settings.DEBUG:
                # draw each point, depending on their color
                for index, point in enumerate(positions):
                    pygame.draw.circle(surface, DEBUG_COLORS[index % len(DEBUG_COLORS)], point, 5)

        for ball in self.balls:
            ball.draw(surface)

        # template
        self.players.append(Player("Simon"))