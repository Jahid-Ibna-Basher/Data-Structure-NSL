import pygame
from paddle import BLACK, Paddle
from ball import Ball
from brick import Brick
pygame.init()
 
# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
 
score = 0
lives = 3
livesP = 10
 
# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

sprites_list = pygame.sprite.Group()

fallenBrick = pygame.sprite.Group()

A = Paddle(WHITE, 100, 10)
A.rect.x = 350
A.rect.y = 560

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()

t = 5
for i in range(24):
    brick = Brick(RED,30,30)
    brick.rect.x = t + i*3 + i*30 #   60 + i* 100
    brick.rect.y = 60
    sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(24):
    brick = Brick(ORANGE,30,30)
    brick.rect.x = t + i*3 + i*30  #60 + i* 100
    brick.rect.y = 100
    sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(24):
    brick = Brick(YELLOW,30,30)
    brick.rect.x = t + i*3 + i*30  #60 + i* 100
    brick.rect.y = 140
    sprites_list.add(brick)
    all_bricks.add(brick)



sprites_list.add(A)
sprites_list.add(ball)
 
carryOn = True

i = 0
 
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        A.moveLeft(8)
    if keys[pygame.K_RIGHT]:
        A.moveRight(8)
 
    sprites_list.update()

    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>=590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            carryOn = False

    if ball.rect.y<=60:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, A):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    
    
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.Fall()
      
      fallenBrick.add(brick)
      
      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
            
    paddle_collision = pygame.sprite.spritecollide(A,fallenBrick,False)
    
    for brick in paddle_collision:
        livesP -= 1
        
        brick.kill()
        
        if livesP == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            carryOn = False
        
        
            
    

  
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives)+'    Paddle-Health: '+str(livesP), 1, WHITE)
    screen.blit(text, (550,10))


    sprites_list.draw(screen)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()