import pygame
from constants import BLOCK_SIZE, WHITE

def draw_block(screen, x, y, color, block_size):
    """
    Draw a single block at grid coordinates (x, y) with the given color and block size.
    """
    pygame.draw.rect(
        screen,
        color,
        (x * block_size, y * block_size, block_size, block_size),
    )

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

def draw_button(screen, text, rect, font, color, bg_color):
    pygame.draw.rect(screen, bg_color, rect)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    screen.blit(text_surf, text_rect)
