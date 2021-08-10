import pygame

BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self,color,w,h):

        super().__init__()

        self.image = pygame.Surface([w,h])

        self.image.fill (BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image,color,[0,0,w,h])

        self.rect = self.image.get_rect()


    def moveLeft(self, pixels):
        self.rect.x = max(self.rect.x - pixels ,0)

    def moveRight(self, pixels):
        self.rect.x = min(self.rect.x + pixels ,700)
        
    def collide(self,brick):
        if brick.rect.x>= self.rect.x and brick.rect.x<= self.rect.x + 100  and brick.rect.y>= self.rect.y:
            return True
        return False
            

        


