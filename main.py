import pygame
import Screen
import time
import consts

pygame.init()

win = Screen.screen
win2 = Screen.screen
x_s = consts.SOLDIER_MIDBOTTOM_X
y_s = consts.SOLDIER_MIDBOTTOM_Y
x_n = consts.NIGHT_SOLDIER_MIDBOTTOM_X
y_n = consts.NIGHT_SOLDIER_MIDBOTTOM_Y
x_f=consts.FLAG_MIDBOTTOM_X
y_f=consts.FLAG_MIDBOTTOM_Y

width = consts.SOLDIER_WIDTH
height = consts.SOLDIER_HEIGHT

img_soldier = Screen.create_soldier(consts.SOLDIER_IMG)
img_flag = Screen.create_flag(consts.FLAG_IMG)
img_night_soldier=Screen.create_soldier(consts.NIGHT_SOLDIER_IMG)
clock = pygame.time.Clock()

vel = 5
run = True

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_s > 0:
        x_s -= vel
        x_n -= vel
    if keys[pygame.K_RIGHT] and x_s < consts.SCREEN_WIDTH - width:
        x_s += vel
        x_n += vel
    if keys[pygame.K_UP] and y_s > 0:
        y_s -= vel
        y_n -= vel
    if keys[pygame.K_DOWN] and y_s < consts.SCREEN_HEIGHT - height:
        y_s += vel
        y_n += vel

    if keys[pygame.K_RETURN]:
        win2 = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        Screen.draw2(img_night_soldier, x_n, y_n, )
        time.sleep(1)
        win = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

    Screen.draw(img_soldier, x_s, y_s,img_flag, x_f, y_f)
    
pygame.quit()
