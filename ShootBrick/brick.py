import pygame, numpy as np
BLACK = (0,0,0)

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, w,h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, w, h])

        self.rect = self.image.get_rect()

        self.velocity = [0,0]

        
    def update(self):

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def Fall(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = np.random.choice([2,3,4])
        
    


