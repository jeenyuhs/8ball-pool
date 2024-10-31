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
    
    def get_shooter(self) -> Player:
        for player in self.players:
            if player.is_shooting:
                return player
    
    def get_who_is_waiting(self) -> Player:
        for player in self.players:
            if not player.is_shooting:
                return player
            
    def get_winner(self) -> Player | None:
        for player in self.players:
            if player.won:
                return player
            
    def get_loser(self) -> Player | None:
        for player in self.players:
            if player.lost:
                return player
    
    def take_turns(self) -> None:
        for player in self.players:
            if player.is_shooting:
                player.is_shooting = False
            elif not player.is_shooting:
                player.is_shooting = True

    def initialize_balls(self) -> None:
        positions = []
        diameter = settings.BALL_RADIUS * 2
        columns = 5
        for i in range(columns):
            for j in range(columns - i):
                x = i * diameter
                y = j * diameter + i * (diameter / 2)
                positions.append((x + settings.SCREEN_WIDTH / 4, y + (settings.SCREEN_HEIGHT - settings.BOTTOM_PANEL_PADDING) // 2 - diameter * 2.5))

        for ball in range(15):
            ball_type = BallType.SOLID
            
            if ball + 1 == 8:
                ball_type = BallType.EIGHT_BALL
            
            if ball + 1 > 8:
                ball_type = BallType.STRIPE

            ball_obj = Ball.create(positions[ball], ball_type)
            ball_obj.image = pygame.image.load(f"assets/images/balls/ball_{ball + 1}.png").convert_alpha()

            self.balls.append(ball_obj)

        cue_ball = Ball.create(
            (
                settings.SCREEN_WIDTH / 1.5, 
                (settings.SCREEN_HEIGHT - settings.BOTTOM_PANEL_PADDING) // 2
            ), 
            type = BallType.CUE
        )
        cue_ball.image = pygame.image.load(f"assets/images/balls/cue_ball.png").convert_alpha()

        self.balls.append(cue_ball)

    def initialize_players(self) -> None:
        self.players.append(Player("Simon", True))
        self.players.append(Player("Noob"))

    def draw(self, surface: pygame.Surface, table_image, wood_panel_image, font) -> None:
        surface.blit(wood_panel_image, (0, 0))
        surface.blit(table_image, (0, 0))

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

        for i, player in enumerate(self.players):
            player.draw(surface, (settings.SCREEN_WIDTH / (3 * (i + 1) / 2), settings.SCREEN_HEIGHT - settings.BOTTOM_PANEL_PADDING / 2), font)