import pygame


class Table:
    def __init__(self):
        self.balls = []

    def create(screen) -> None:
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 400

        POCKET_RADIUS = 20
        BORDER_THICKNESS = 30

        GREEN = (34, 139, 34)
        DARKER_GREEN = (28, 115, 66)
        WOOD = (139, 69, 19)
        BLACK = (0, 0, 0)

        # felt
        pygame.draw.rect(
            screen,
            GREEN,
            (
                BORDER_THICKNESS,
                BORDER_THICKNESS,
                SCREEN_WIDTH - 2 * BORDER_THICKNESS,
                SCREEN_HEIGHT - 2 * BORDER_THICKNESS,
            ),
        )

        # borders
        pygame.draw.rect(screen, WOOD, (0, 0, SCREEN_WIDTH, BORDER_THICKNESS))
        pygame.draw.rect(
            screen,
            WOOD,
            (0, SCREEN_HEIGHT - BORDER_THICKNESS, SCREEN_WIDTH, BORDER_THICKNESS),
        )
        pygame.draw.rect(screen, WOOD, (0, 0, BORDER_THICKNESS, SCREEN_HEIGHT))
        pygame.draw.rect(
            screen,
            WOOD,
            (SCREEN_WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, SCREEN_HEIGHT),
        )

        pockets = [
            (BORDER_THICKNESS, BORDER_THICKNESS),
            (SCREEN_WIDTH // 2, BORDER_THICKNESS),
            (SCREEN_WIDTH - BORDER_THICKNESS, BORDER_THICKNESS),
            (BORDER_THICKNESS, SCREEN_HEIGHT - BORDER_THICKNESS),
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT - BORDER_THICKNESS),
            (SCREEN_WIDTH - BORDER_THICKNESS, SCREEN_HEIGHT - BORDER_THICKNESS),
        ]

        for pocket in pockets:
            pygame.draw.circle(screen, BLACK, pocket, POCKET_RADIUS)

        # what is the name of them?
        LENGTH_OF_SLABS = 10

        # fmt: off
        slab_positions = [
            [
                [BORDER_THICKNESS + POCKET_RADIUS, BORDER_THICKNESS],
                [BORDER_THICKNESS + POCKET_RADIUS + 15, BORDER_THICKNESS + LENGTH_OF_SLABS],
                [SCREEN_WIDTH // 2 - POCKET_RADIUS - 5, BORDER_THICKNESS + LENGTH_OF_SLABS],
                [SCREEN_WIDTH // 2 - POCKET_RADIUS, BORDER_THICKNESS],
            ],
            [
                [SCREEN_WIDTH // 2 + POCKET_RADIUS, BORDER_THICKNESS],
                [SCREEN_WIDTH // 2 + POCKET_RADIUS + 5,BORDER_THICKNESS + LENGTH_OF_SLABS],
                [SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS - 15, BORDER_THICKNESS + LENGTH_OF_SLABS],
                [SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS, BORDER_THICKNESS],
            ],
            [
                [SCREEN_WIDTH - BORDER_THICKNESS, BORDER_THICKNESS + POCKET_RADIUS],
                [SCREEN_WIDTH - BORDER_THICKNESS - LENGTH_OF_SLABS, BORDER_THICKNESS + POCKET_RADIUS + 15],
                [SCREEN_WIDTH - BORDER_THICKNESS - LENGTH_OF_SLABS, SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS - 15],
                [SCREEN_WIDTH - BORDER_THICKNESS, SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS],
            ],
            [
                [SCREEN_WIDTH // 2 + POCKET_RADIUS, SCREEN_HEIGHT - BORDER_THICKNESS],
                [SCREEN_WIDTH // 2 + POCKET_RADIUS + 5, SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS],
                [SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS - 15, SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS],
                [SCREEN_WIDTH - BORDER_THICKNESS - POCKET_RADIUS, SCREEN_HEIGHT - BORDER_THICKNESS],
            ],
            [
                [BORDER_THICKNESS + POCKET_RADIUS, SCREEN_HEIGHT - BORDER_THICKNESS],
                [BORDER_THICKNESS + POCKET_RADIUS + 15, SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS],
                [SCREEN_WIDTH // 2 - POCKET_RADIUS - 5, SCREEN_HEIGHT - BORDER_THICKNESS - LENGTH_OF_SLABS],
                [SCREEN_WIDTH // 2 - POCKET_RADIUS, SCREEN_HEIGHT - BORDER_THICKNESS],
            ],
            [
                [BORDER_THICKNESS, BORDER_THICKNESS + POCKET_RADIUS],
                [BORDER_THICKNESS + LENGTH_OF_SLABS, BORDER_THICKNESS + POCKET_RADIUS + 15],
                [BORDER_THICKNESS + LENGTH_OF_SLABS, SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS - 15],
                [BORDER_THICKNESS, SCREEN_HEIGHT - BORDER_THICKNESS - POCKET_RADIUS],
            ],
        ]

        for position in slab_positions:
            pygame.draw.polygon(screen, DARKER_GREEN, position)
