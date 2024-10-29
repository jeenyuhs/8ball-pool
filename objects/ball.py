import pymunk

import utils


class Ball:
    # def __init__(self) -> None:
    #     self.x = 0
    #     self.y = 0
    #     self.dx = 0
    #     self.dy = 0

    #     self.speed = 0
    #     self.angle = 0

    @staticmethod
    def create(position: tuple[int, int, int]) -> pymunk.Shape:
        body = pymunk.Body()
        body.position = position

        shape = pymunk.Circle(body, 18.75)
        shape.mass = 5
        shape.elasticity = 0.8

        pivot = pymunk.PivotJoint(utils.SPACE.static_body, body, (0, 0), (0 , 0))
        pivot.max_bias = 0
        pivot.max_force = 1000

        utils.SPACE.add(body, shape, pivot)
        return shape

