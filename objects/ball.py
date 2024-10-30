from enum import IntEnum
import pymunk

import settings
import utils

class BallType(IntEnum):
    CUE = 0
    SOLID = 1
    STRIPE = 2

    EIGHT_BALL = 3

class Ball(pymunk.Shape):
    def __init__(self, shape: pymunk.Shape) -> None:
        super().__init__(shape)

        self.type: BallType = BallType.SOLID
        self.image = None 

    @classmethod
    def create(cls, position: tuple[int, int, int], type: BallType) -> "Ball":
        body = pymunk.Body()
        body.position = position

        shape = pymunk.Circle(body, settings.BALL_RADIUS)
        shape.mass = 1
        shape.elasticity = 0.8

        pivot = pymunk.PivotJoint(utils.SPACE.static_body, body, (0, 0), (0, 0))
        pivot.max_bias = 0
        pivot.max_force = 2000

        utils.SPACE.add(body, shape, pivot)

        ball = cls(shape)
        ball.type = type

        return ball

