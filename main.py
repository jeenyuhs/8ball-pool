import pygame
from objects.table import Table


def game():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("8-BALL")

    WOOD = (139, 69, 19)  # Border color

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WOOD)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Table.create(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    game()
