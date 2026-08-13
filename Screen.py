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
