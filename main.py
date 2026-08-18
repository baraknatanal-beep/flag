import pygame
import Screen
import time
import consts
import soldier
import csv
import pandas as pd
pygame.font.init()
pygame.init()

dis = Screen.screen
dis2 = Screen.screen
win=Screen.screen
x_s = soldier.SOLDIER_MIDBOTTOM_X
y_s = soldier.SOLDIER_MIDBOTTOM_Y
x_n = soldier.NIGHT_SOLDIER_MIDBOTTOM_X
y_n = soldier.NIGHT_SOLDIER_MIDBOTTOM_Y
x_f=consts.FLAG_MIDBOTTOM_X
y_f=consts.FLAG_MIDBOTTOM_Y
grass=Screen.grass_surface

width = consts.SOLDIER_WIDTH
height = consts.SOLDIER_HEIGHT

img_soldier = Screen.create_soldier(soldier.SOLDIER_IMG)
img_flag = Screen.create_flag(consts.FLAG_IMG)
img_night_soldier=Screen.create_soldier(soldier.NIGHT_SOLDIER_IMG)
clock = pygame.time.Clock()
mine=soldier.mine_extension()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Some Text', False, (0, 0, 0))
vel = 5
run = True
Screen.welcome_message(img_soldier, x_s, y_s,img_flag, x_f, y_f)
game_saves={}
while run:
    current_time = pygame.time.get_ticks()
    clock.tick(10)
    body_lst = soldier.body_lst(x_s, y_s)
    legs_lst=soldier.legs_lst(x_s, y_s)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                key_pressed_time = pygame.time.get_ticks()
        elif event.type == pygame.KEYUP:
            if pygame.K_1 <= event.key <= pygame.K_9 and key_pressed_time > 0:
                hold_duration = (pygame.time.get_ticks() - key_pressed_time) / 1000
                key_pressed_time = 0
                if hold_duration >= 1.0:
                    game_saves[f"{pygame.key.name(event.key)}"]= x_s, y_s, x_f, y_f,grass,mine
                    with open("test2.csv", "a", newline="") as f:
                        w = csv.DictWriter(f, game_saves.keys())
                        w.writeheader()
                        w.writerow(game_saves)
                else:
                    l=False
                    with open("test2.csv", 'r') as data:
                        for line in csv.reader(data):
                            if l==True:
                                x_s, y_s,x_f, y_f= int(line[0][1:-1].split(",")[0]),int(line[0][1:-1].split(",")[1]),int(line[0][1:-1].split(",")[2]),int(line[0][1:-1].split(",")[3])
                                x_n, y_n,=x_s,y_s
                                grass=line[0][1:-1].split(",")[4]
                                mine=line[0][1:-1].split(",")[5]

                                print(x_s, y_s, x_f, y_f)
                                l=False
                            if line[0]==pygame.key.name(event.key):
                                l=True
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
    if soldier.touch_flag(body_lst, soldier.flag_lst):
        Screen.winning_message()
        exit()
    if soldier.touch_mine(legs_lst, mine):
        Screen.loosing_message()

    if keys[pygame.K_RETURN]:
        dis2 = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        Screen.draw2(img_night_soldier, x_n, y_n, )
        time.sleep(1)
        dis = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
    Screen.draw(img_soldier, x_s, y_s,img_flag, x_f, y_f)

pygame.quit()
