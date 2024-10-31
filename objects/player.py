from objects.ball import Ball, BallType


class Player:
    def __init__(self, username: str) -> None:
        self.username: str = username
        self.potted_balls: list[Ball] = []

        self.is_shooting: bool = False
        self.has_ball_type: BallType | None = None
        self.has_potted_new_balls: bool = False
