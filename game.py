import pygame
import random
from constants import GRID_WIDTH, GRID_HEIGHT, SHAPES, WHITE, RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE, BLACK
from grid import initialize_grid, draw_grid, place_shape_on_grid
from utils import rotate_shape, check_collision, check_game_over, draw_block  # Import draw_block

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * 25, GRID_HEIGHT * 25))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
    current_shape = random.choice(SHAPES)
    current_color = random.choice([RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE])
    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

    # Timing variables for block descent and input handling
    normal_tick_rate = 500  # milliseconds for regular descent
    fast_tick_rate = 100    # milliseconds for faster descent
    last_tick = pygame.time.get_ticks()

    horizontal_move_delay = 150  # milliseconds delay for horizontal movement
    last_horizontal_move = pygame.time.get_ticks()

    rotation_delay = 200  # milliseconds delay for rotation
    last_rotation_time = pygame.time.get_ticks()

    game_over = False
    while not game_over:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # Handle horizontal movement with delay
        if current_time - last_horizontal_move > horizontal_move_delay:
            if keys[pygame.K_LEFT] and not check_collision(grid, current_shape, shape_x - 1, shape_y):
                shape_x -= 1
                last_horizontal_move = current_time
            if keys[pygame.K_RIGHT] and not check_collision(grid, current_shape, shape_x + 1, shape_y):
                shape_x += 1
                last_horizontal_move = current_time

        # Handle rotation with delay
        if keys[pygame.K_UP] and current_time - last_rotation_time > rotation_delay:
            rotated = rotate_shape(current_shape)
            if not check_collision(grid, rotated, shape_x, shape_y):
                current_shape = rotated
                last_rotation_time = current_time

        # Determine descent rate based on whether the down arrow is pressed
        current_tick_rate = fast_tick_rate if keys[pygame.K_DOWN] else normal_tick_rate

        # Handle automatic downward movement
        if current_time - last_tick > current_tick_rate:
            if not check_collision(grid, current_shape, shape_x, shape_y + 1):
                shape_y += 1
            else:
                place_shape_on_grid(grid, current_shape, shape_x, shape_y, current_color)
                if check_game_over(grid):
                    game_over = True
                else:
                    shape_y = 0
                    shape_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
                    current_shape = random.choice(SHAPES)
                    current_color = random.choice([RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE])
            last_tick = current_time

        screen.fill(BLACK)
        draw_grid(screen, grid, 25)

        # Draw current shape
        for y, row in enumerate(current_shape):
            for x, value in enumerate(row):
                if value:
                    draw_block(screen, shape_x + x, shape_y + y, current_color)

        pygame.display.flip()
        clock.tick(30)

    # Display "Game Over" message
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (GRID_WIDTH * 25 // 2 - 50, GRID_HEIGHT * 25 // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
