import pymunk
import pymunk.pygame_util

SPACE = pymunk.Space()

SLABS = (
    ((122, 79), (146, 100), (761, 100), (766, 86), (766, 77)),
    ((830, 77), (830, 86), (834, 100), (1451, 100), (1476, 77)),
    ((1520, 117), (1495, 145), (1495, 746), (1520, 775)),
    ((1477, 816), (1452, 795), (834, 795), (830, 815)),
    ((766, 816), (766, 810), (762, 795), (144, 795), (119, 816)),
    ((77, 774), (100, 751), (100, 147), (78, 117))
)

def initialize_slab_collision_detection() -> None:
    for positions in SLABS:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = ((0, 0))

        shape = pymunk.Poly(body, positions)
        shape.elasticity = 0.5

        SPACE.add(body, shape)