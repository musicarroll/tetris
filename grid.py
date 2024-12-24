import pygame
from constants import BLACK, WHITE

def initialize_grid(width, height):
    return [[(0, BLACK) for _ in range(width)] for _ in range(height)]

def draw_grid(screen, grid, block_size):
    for x in range(0, len(grid[0]) * block_size, block_size):
        pygame.draw.line(screen, WHITE, (x, 0), (x, len(grid) * block_size))
    for y in range(0, len(grid) * block_size, block_size):
        pygame.draw.line(screen, WHITE, (0, y), (len(grid[0]) * block_size, y))

    for y, row in enumerate(grid):
        for x, (filled, color) in enumerate(row):
            if filled:
                pygame.draw.rect(screen, color, (x * block_size, y * block_size, block_size, block_size))

def place_shape_on_grid(grid, shape, x, y, color):
    for dy, row in enumerate(shape):
        for dx, value in enumerate(row):
            if value:
                grid[y + dy][x + dx] = (1, color)
