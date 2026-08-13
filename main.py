import pygame
from pygame import display
import Screen
import time
import consts

pygame.init()

win = Screen.screen
x = consts.SOLDIER_MIDBOTTOM_X
y = consts.SOLDIER_MIDBOTTOM_Y

width = consts.SOLDIER_WIDTH
height = consts.SOLDIER_HEIGHT

img = Screen.create_soldier(consts.SOLDIER_IMG)

clock = pygame.time.Clock()

vel = 5
run = True

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < consts.SCREEN_WIDTH - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < consts.SCREEN_HEIGHT - height:
        y += vel

    if keys[pygame.K_RETURN]:
        display2 = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        time.sleep(1)
        win = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

    Screen.draw(img, x, y)

pygame.quit()
