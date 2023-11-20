import pygame
from pygame.locals import(K_ESCAPE,KEYDOWN)
pygame.init()

SCREEN_LENGTH = 1000
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_LENGTH,SCREEN_WIDTH))

player = pygame.Rect((300,300,30,30))


running = True

while running:
 

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,0,0),player)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1,0)
    elif key[pygame.K_UP] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0,1)



for event in pygame.event.get():
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()


 
 

