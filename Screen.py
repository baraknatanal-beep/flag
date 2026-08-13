import random
import pygame
import consts

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

GRASS_POSITIONS = []
for i in range(20):
    x = random.randint(0, consts.SCREEN_WIDTH - consts.GRASS_WIDTH)
    y = random.randint(0, consts.SCREEN_HEIGHT - consts.SOLDIER_HEIGHT)
    GRASS_POSITIONS.append((x, y))


def create_soldier(soldier_img):
    sized_soldier = pygame.transform.scale(soldier_img, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    return sized_soldier


def draw_soldier(soldier, x, y):
    screen.blit(soldier, (x, y))


def create_grass(grass_img):
    sized_grass = pygame.transform.scale(grass_img, (consts.GRASS_WIDTH, consts.SOLDIER_HEIGHT))
    return sized_grass


def draw_grass(grass):
    for pos in GRASS_POSITIONS:
        screen.blit(grass, pos)


grass_surface = create_grass(consts.GRASS_IMG)


def draw(soldier_img, soldier_x, soldier_y):
    screen.fill(consts.BACKGROUND_COLOR)

    draw_grass(grass_surface)

    draw_soldier(soldier_img, soldier_x, soldier_y)

    pygame.display.update()
