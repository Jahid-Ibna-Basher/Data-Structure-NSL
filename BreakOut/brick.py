import pygame
BLACK = (0,0,0)

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, w,h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, w, h])

        self.rect = self.image.get_rect()


