import pygame
import numpy as np

from random import randint
BLACK = (0,0,0)
 
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [3,np.random.choice([2,3,4,5,-2,-3,-4,-5])]
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = np.random.choice([2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9])
