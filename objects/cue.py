import pygame


class Cue:
    def __init__(self, image, position: tuple[int, int, int]) -> None: 
        self.referenced_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.referenced_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, surface) -> None:
        self.image = pygame.transform.rotate(self.referenced_image, self.angle)
        surface.blit(
            self.image, 
            (
                self.rect.centerx - self.image.get_width() / 2, 
                self.rect.centery - self.image.get_height() / 2
            )
        )