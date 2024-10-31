import pygame
import pymunk
import pymunk.pygame_util

SPACE = pymunk.Space()

SLABS = (
    ((113, 72), (139, 92), (758, 92), (763, 68)),
    ((827, 69), (832, 92), (1452, 92), (1479, 69)),
    ((1524, 109), (1500, 139), (1500, 748), (1524, 775)),
    ((1481, 817), (1455, 795), (832, 795), (828, 817)),
    ((763, 817), (758, 795), (135, 795), (111, 816)),
    ((68, 775), (90, 751), (90, 139), (69, 110))
)

def initialize_slab_collision_detection() -> None:
    for positions in SLABS:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = ((0, 0))

        shape = pymunk.Poly(body, positions)
        shape.elasticity = 0.8

        SPACE.add(body, shape)