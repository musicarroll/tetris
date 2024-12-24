import pygame
from constants import BLOCK_SIZE, WHITE

def draw_block(screen, x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def rotate_shape(shape):
    return list(zip(*reversed(shape)))

def check_collision(grid, shape, x, y):
    for dy, row in enumerate(shape):
        for dx, value in enumerate(row):
            if value and (x + dx < 0 or x + dx >= len(grid[0]) or y + dy >= len(grid) or grid[y + dy][x + dx][0]):
                return True
    return False

def check_game_over(grid):
    return any(grid[0][x][0] for x in range(len(grid[0])))
