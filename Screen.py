import random
import time

import pygame
import consts
import soldier
from random import randrange
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

GRASS_POSITIONS = []
for i in range(20):
    x = random.randrange(0, consts.SCREEN_WIDTH - consts.GRASS_WIDTH,25*3)
    y = random.randrange(0, consts.SCREEN_HEIGHT - consts.SOLDIER_HEIGHT,25)
    GRASS_POSITIONS.append((x, y))
MINE_POSITIONS = []
for i in range(20):
    x_l = random.randrange(100, consts.SCREEN_WIDTH - consts.MINE_WIDTH,25*3)
    y_l = random.randrange(100, consts.SCREEN_HEIGHT - consts.SOLDIER_HEIGHT,25)
    MINE_POSITIONS.append((x_l, y_l))

def create_soldier(soldier_img):
    sized_soldier = pygame.transform.scale(soldier_img, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    return sized_soldier


def draw_soldier(soldier, x, y):
    screen.blit(soldier, (x, y))


def create_grass(grass_img):
    sized_grass = pygame.transform.scale(grass_img, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    return sized_grass

def draw_grass(grass):
    for pos in GRASS_POSITIONS:
        screen.blit(grass, pos)

grass_surface = create_grass(consts.GRASS_IMG)
def create_mine(mine_img):
    sized_mine = pygame.transform.scale(mine_img, (consts.MINE_WIDTH, consts.MINE_HEIGHT))
    return sized_mine

def draw_mine(mine):
    for pos in MINE_POSITIONS:
        screen.blit(mine, pos)

mine_surface = create_mine(consts.MINE_IMG)

def create_flag (flag_img,):
    sized_flag=pygame.transform.scale(flag_img,(consts.FLAG_WIDTH,consts.FLAG_HEIGHT))
    return sized_flag

def draw_flag(flag,x,y):
    screen.blit(flag, (x,y))

def create_matrix():
    matrix_surface = pygame.Surface((consts.SCREEN_WIDTH, consts.GRID_ROWS * consts.CELL_SIZE), pygame.SRCALPHA)
    matrix_surface.fill((0, 0, 0))
    for r in range(consts.GRID_ROWS + 1):
        start_pos = (0, r * consts.CELL_SIZE)
        end_pos = (consts.SCREEN_WIDTH, r * consts.CELL_SIZE)
        pygame.draw.line(screen, (100, 100, 100), start_pos, end_pos, 1)

    for c in range(consts.GRID_COLS + 1):
        start_pos = (c * consts.CELL_SIZE, 0)
        end_pos = (c * consts.CELL_SIZE, consts.GRID_ROWS * consts.CELL_SIZE)
        pygame.draw.line(screen, (100, 100, 100), start_pos, end_pos, 1)
    return matrix_surface

def winning_message():
    black = (0, 0, 0)
    green = (0, 255, 0)
    display_surface = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render('you win', True, green)
    textRect = text.get_rect()
    textRect.center = (consts.SCREEN_WIDTH // 2, consts.SCREEN_HEIGHT // 2)
    while True:
        display_surface.fill(black)
        display_surface.blit(text, textRect)
        pygame.display.update()
        time.sleep(3)
        quit()


def loosing_message():
    display_surface = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render('you  landed on  a  landmine', True, (255,0,0))
    textRect = text.get_rect()
    textRect.center = (consts.SCREEN_WIDTH // 2, consts.SCREEN_HEIGHT // 2)
    while True:
        display_surface.fill((0,0,0))
        display_surface.blit(text, textRect)
        pygame.display.update()
        time.sleep(3)
        quit()
def welcome_message(soldier_img, soldier_x, soldier_y,flag_img, flag_x, flag_y):
    display_surface = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('freesansbold.ttf', 30 )
    text = font.render('welcome to the game', True,(255,255,255))
    textRect = text.get_rect()
    textRect.center = (150, 50)
    while True:
        draw(soldier_img, soldier_x, soldier_y,flag_img, flag_x, flag_y)
        display_surface.blit(text, textRect)
        pygame.display.update()
        time.sleep(3)
        break
def draw(soldier_img, soldier_x, soldier_y,flag_img, flag_x, flag_y):

    screen.fill(consts.BACKGROUND_COLOR)

    draw_grass(grass_surface)

    draw_soldier(soldier_img, soldier_x, soldier_y)

    draw_flag(flag_img, flag_x, flag_y)

    pygame.display.update()

def draw2(soldier_img, soldier_x, soldier_y):
    screen.fill((0,0,0))

    create_matrix()

    draw_mine(mine_surface)

    draw_soldier(soldier_img, soldier_x, soldier_y)

    pygame.display.update()
