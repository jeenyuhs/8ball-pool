import pymunk
import pymunk.pygame_util

import settings


SPACE = pymunk.Space()

def initialize_slab_collision_detection() -> None:
    # redo
    BORDER_THICKNESS = 50
    POCKET_RADIUS = 30
    LENGTH_OF_SLABS = 20

    slab_positions = (
        (
            (BORDER_THICKNESS + POCKET_RADIUS, BORDER_THICKNESS),
            (BORDER_THICKNESS + POCKET_RADIUS + 15, BORDER_THICKNESS + LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH // 2 - POCKET_RADIUS - 5, BORDER_THICKNESS + LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH // 2 - POCKET_RADIUS + 1.2, BORDER_THICKNESS),
        ),
        (
            (settings.SCREEN_WIDTH // 2 + POCKET_RADIUS - 1.2, BORDER_THICKNESS),
            (settings.SCREEN_WIDTH // 2 + POCKET_RADIUS + 5, BORDER_THICKNESS + LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS - 20, BORDER_THICKNESS + LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS, BORDER_THICKNESS),
        ),
        (
            (settings.SCREEN_WIDTH - BORDER_THICKNESS, BORDER_THICKNESS + POCKET_RADIUS),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS - LENGTH_OF_SLABS, BORDER_THICKNESS + POCKET_RADIUS + 20),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS - LENGTH_OF_SLABS, settings.SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS - 20),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS, settings.SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS),
        ),
        (
            (settings.SCREEN_WIDTH // 2 + POCKET_RADIUS - 1.2, settings.SCREEN_HEIGHT - BORDER_THICKNESS),
            (settings.SCREEN_WIDTH // 2 + POCKET_RADIUS + 5, settings.SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS - 20, settings.SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS, settings.SCREEN_HEIGHT - BORDER_THICKNESS),
        ),
        (
            (BORDER_THICKNESS + POCKET_RADIUS, settings.SCREEN_HEIGHT - BORDER_THICKNESS),
            (BORDER_THICKNESS + POCKET_RADIUS + 20, settings.SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH // 2 - POCKET_RADIUS - 5, settings.SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS),
            (settings.SCREEN_WIDTH // 2 - POCKET_RADIUS + 1.2, settings.SCREEN_HEIGHT - BORDER_THICKNESS),
        ),
        (
            (BORDER_THICKNESS, BORDER_THICKNESS + POCKET_RADIUS),
            (BORDER_THICKNESS + LENGTH_OF_SLABS, BORDER_THICKNESS + POCKET_RADIUS + 20),
            (BORDER_THICKNESS + LENGTH_OF_SLABS, settings.SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS - 20),
            (BORDER_THICKNESS, settings.SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS),
        ),
    )

    for slab in slab_positions:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = ((0, 0))

        shape = pymunk.Poly(body, slab)
        shape.elasticity = 0.5

        SPACE.add(body, shape)