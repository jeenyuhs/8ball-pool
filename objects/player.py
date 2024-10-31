from dataclasses import dataclass
from enum import IntEnum
from objects.ball import Ball, BallType

class FoulType(IntEnum):
    POTTED_CUE_BALL = 0
    POTTED_WRONG_BALL = 1
    HIT_WRONG_FIRST = 2
    POTTED_8BALL_EARLY = 3

class Player:
    def __init__(self, username: str) -> None:
        self.username: str = username
        self.potted_balls: list[Ball] = []

        self.is_shooting: bool = False
        self.has_ball_type: BallType | None = None
        self.has_potted_new_balls: bool = False
