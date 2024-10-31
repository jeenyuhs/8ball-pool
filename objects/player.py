from dataclasses import dataclass
from enum import IntEnum

from pygame import Surface
from objects.ball import Ball, BallType
import utils

class FoulType(IntEnum):
    POTTED_CUE_BALL = 0
    POTTED_WRONG_BALL = 1
    HIT_WRONG_FIRST = 2
    POTTED_8BALL_EARLY = 3

class Player:
    def __init__(self, username: str, is_shooting: bool = False) -> None:
        self.username: str = username
        self.potted_balls: list[Ball] = []

        self.is_shooting: bool = is_shooting
        self.has_ball_type: BallType | None = None
        self.has_potted_new_balls: bool = False

        self.won: bool = False
        self.lost: bool = False

    def draw(self, surface: Surface, position: tuple[int, int], font) -> None:
        color = (0, 255, 0) if self.is_shooting else (0, 0, 0)
        text_surface = font.render(self.username, False, color)
        surface.blit(text_surface, position)
        
        for i, potted_ball in enumerate(self.potted_balls):
            draw_at = (position[0] + (20 * i), position[1] + 30)
            surface.blit(potted_ball.image, draw_at)
