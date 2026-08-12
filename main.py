
import pygame
import time
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving rectangle")

x = 200
y = 200

width = 20
height = 20

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
        x -= 1

    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += 1

    if keys[pygame.K_UP] and y > 0:
        y -= 1

    if keys[pygame.K_DOWN] and y < 500 - height:
        y += 1
    if keys[pygame.K_RETURN] :
        display2 = pygame.display.set_mode((600, 600))
        time.sleep(1)
        win = pygame.display.set_mode((500, 500))
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


