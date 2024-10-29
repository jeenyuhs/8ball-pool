import pygame

import settings


class Table:
    def __init__(self):
        self.balls = []

    @staticmethod
    def draw(screen) -> None:
        POCKET_RADIUS = 30
        BORDER_THICKNESS = 50

        GREEN = settings.COLORS["GREEN"]
        DARKER_GREEN = settings.COLORS["DARKER_GREEN"]
        WOOD = settings.COLORS["WOOD"]
        BLACK = settings.COLORS["BLACK"]

        # felt
        pygame.draw.rect(
            screen,
            GREEN,
            (
                BORDER_THICKNESS,
                BORDER_THICKNESS,
                settings.SCREEN_WIDTH - 2 * BORDER_THICKNESS,
                settings.SCREEN_HEIGHT - 2 * BORDER_THICKNESS,
            ),
        )

        # borders
        pygame.draw.rect(screen, WOOD, (0, 0, settings.SCREEN_WIDTH, BORDER_THICKNESS))
        pygame.draw.rect(
            screen,
            WOOD,
            (0, settings.SCREEN_HEIGHT - BORDER_THICKNESS, settings.SCREEN_WIDTH, BORDER_THICKNESS),
        )
        pygame.draw.rect(screen, WOOD, (0, 0, BORDER_THICKNESS, settings.SCREEN_HEIGHT))
        pygame.draw.rect(
            screen,
            WOOD,
            (settings.SCREEN_WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, settings.SCREEN_HEIGHT),
        )
    
        # funny thing about the middle pockets, is that they're not
        # alligned with their corner counterparts.

        # fmt: off
        pockets = (
            (BORDER_THICKNESS, BORDER_THICKNESS),
            (settings.SCREEN_WIDTH // 2, BORDER_THICKNESS - 12),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS, BORDER_THICKNESS),
            (BORDER_THICKNESS, settings.SCREEN_HEIGHT - BORDER_THICKNESS),
            (settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - BORDER_THICKNESS + 12),
            (settings.SCREEN_WIDTH - BORDER_THICKNESS, settings.SCREEN_HEIGHT - BORDER_THICKNESS),
        )

        for pocket in pockets:
            pygame.draw.circle(screen, BLACK, pocket, POCKET_RADIUS)

        # what is the name of them?
        LENGTH_OF_SLABS = 20

        # fmt: off
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

        DEBUG_COLORS = (
            (255, 0, 0),    # red
            (0, 255, 0),    # green
            (0, 0, 255),    # blue
            (255, 255, 0)   # yellow
        )

        for position in slab_positions:
            pygame.draw.polygon(screen, DARKER_GREEN, position)

            if settings.DEBUG:
                # draw each point, depending on their color
                for index, point_position in enumerate(position):
                    pygame.draw.circle(screen, DEBUG_COLORS[index], point_position, 5)
