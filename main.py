import pygame
from pygame import display
import Screen
import pygame
import time
import consts
from Screen import draw
pygame.init()


win=Screen.screen.
x = consts.SOLDIER_MIDBOTTOM_X
y = consts.SOLDIER_MIDBOTTOM_Y

width =consts.SOLDIER_WIDTH
height = consts.SOLDIER_HEIGHT
img=Screen.create_soldier(consts.SOLDIER_IMG)
img=img.get_rect()
vel = 10
run = True
# infinite loop
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= 10

    if keys[pygame.K_RIGHT] and x < consts.SCREEN_WIDTH - width:
        x += 10

    if keys[pygame.K_UP] and y > 0:
        y -= 10

    if keys[pygame.K_DOWN] and y < consts.SCREEN_HEIGHT - height:
        y += 10
    if keys[pygame.K_RETURN] :
        display2 = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
        time.sleep(1)
        win = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
    win.transform(img, (x, y))
    pygame.display.update()