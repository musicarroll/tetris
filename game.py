# import pygame
# import random
# from constants import GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE, SHAPES, SHAPE_COLORS, WHITE, RED, BLUE, BLACK
# from grid import initialize_grid, draw_grid, place_shape_on_grid, clear_full_rows
# from utils import rotate_shape, draw_button, check_collision, check_game_over, draw_block  # Import draw_block
# from time import sleep
# from grid import initialize_grid, draw_grid, draw_preview, place_shape_on_grid, clear_full_rows



# def main():
#     global GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE
#     pygame.init()
#     screen = pygame.display.set_mode((GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), pygame.RESIZABLE)
#     pygame.display.set_caption("Tetris")
#     clock = pygame.time.Clock()

#     font = pygame.font.Font(None, 36)
#     game_over_font = pygame.font.Font(None, 72)

#     # Initialize grid and game variables
#     BLOCK_SIZE = min(screen.get_width() // GRID_WIDTH, screen.get_height() // GRID_HEIGHT)
#     grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
#     current_shape_index = random.randint(0, len(SHAPES) - 1)
#     current_shape = SHAPES[current_shape_index]
#     current_color = SHAPE_COLORS[current_shape_index]
#     shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

#     normal_tick_rate = 500
#     fast_tick_rate = 100
#     last_tick = pygame.time.get_ticks()

#     horizontal_move_delay = 150
#     last_horizontal_move = pygame.time.get_ticks()

#     rotation_delay = 200
#     last_rotation_time = pygame.time.get_ticks()

#     # Scoring and level variables
#     score = 0
#     lines_cleared = 0
#     level = 0

#     game_running = False
#     game_paused = False
#     game_over = False

#     start_button_rect = (50, 10, 100, 50)
#     pause_button_rect = (200, 10, 150, 50)

#     def calculate_score(lines, level):
#         """Calculate score based on lines cleared and level."""
#         line_scores = {1: 40, 2: 100, 3: 300, 4: 1200}
#         return line_scores.get(lines, 0) * (level + 1)

#     while True:
#         current_time = pygame.time.get_ticks()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = event.pos
#                 if start_button_rect[0] <= mouse_x <= start_button_rect[0] + start_button_rect[2] and \
#                    start_button_rect[1] <= mouse_y <= start_button_rect[1] + start_button_rect[3]:
#                     game_running = True
#                     game_over = False
#                     grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
#                     current_shape_index = random.randint(0, len(SHAPES) - 1)
#                     current_shape = SHAPES[current_shape_index]
#                     current_color = SHAPE_COLORS[current_shape_index]
#                     shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
#                     score = 0
#                     lines_cleared = 0
#                     level = 0

#                 if pause_button_rect[0] <= mouse_x <= pause_button_rect[0] + pause_button_rect[2] and \
#                    pause_button_rect[1] <= mouse_y <= pause_button_rect[1] + pause_button_rect[3] and game_running:
#                     game_paused = not game_paused

#             if event.type == pygame.KEYDOWN and game_over:
#                 if event.key == pygame.K_r:  # Restart the game
#                     game_running = True
#                     game_over = False
#                     grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
#                     current_shape_index = random.randint(0, len(SHAPES) - 1)
#                     current_shape = SHAPES[current_shape_index]
#                     current_color = SHAPE_COLORS[current_shape_index]
#                     shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
#                     score = 0
#                     lines_cleared = 0
#                     level = 0

#         if game_running and not game_paused and not game_over:
#             keys = pygame.key.get_pressed()
#             if current_time - last_horizontal_move > horizontal_move_delay:
#                 if keys[pygame.K_LEFT] and not check_collision(grid, current_shape, shape_x - 1, shape_y):
#                     shape_x -= 1
#                     last_horizontal_move = current_time
#                 if keys[pygame.K_RIGHT] and not check_collision(grid, current_shape, shape_x + 1, shape_y):
#                     shape_x += 1
#                     last_horizontal_move = current_time

#             if keys[pygame.K_UP] and current_time - last_rotation_time > rotation_delay:
#                 rotated = rotate_shape(current_shape)
#                 if not check_collision(grid, rotated, shape_x, shape_y):
#                     current_shape = rotated
#                     last_rotation_time = current_time

#             current_tick_rate = fast_tick_rate if keys[pygame.K_DOWN] else normal_tick_rate
#             if current_time - last_tick > current_tick_rate:
#                 if not check_collision(grid, current_shape, shape_x, shape_y + 1):
#                     shape_y += 1
#                 else:
#                     place_shape_on_grid(grid, current_shape, shape_x, shape_y, current_color)
#                     cleared_rows = clear_full_rows(grid)
#                     if cleared_rows > 0:
#                         score += calculate_score(cleared_rows, level)
#                         lines_cleared += cleared_rows
#                         if lines_cleared // 10 > level:
#                             level += 1
#                     if check_game_over(grid):
#                         game_running = False
#                         game_over = True
#                     else:
#                         shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
#                         current_shape_index = random.randint(0, len(SHAPES) - 1)
#                         current_shape = SHAPES[current_shape_index]
#                         current_color = SHAPE_COLORS[current_shape_index]
#                 last_tick = current_time

#         screen.fill(BLACK)

#         draw_button(screen, "Start", start_button_rect, font, WHITE, RED)
#         draw_button(screen, "Pause" if game_running and not game_paused else "Continue",
#                     pause_button_rect, font, WHITE, BLUE)

#         if game_running:
#             draw_grid(screen, grid, BLOCK_SIZE)
#             for y, row in enumerate(current_shape):
#                 for x, value in enumerate(row):
#                     if value:
#                         draw_block(screen, shape_x + x, shape_y + y, current_color, BLOCK_SIZE)

#             # Display score and level
#             score_text = font.render(f"Score: {score}", True, WHITE)
#             level_text = font.render(f"Level: {level}", True, WHITE)
#             lines_text = font.render(f"Lines: {lines_cleared}", True, WHITE)
#             screen.blit(score_text, (10, 50))
#             screen.blit(level_text, (10, 80))
#             screen.blit(lines_text, (10, 110))

#         if game_over:
#             game_over_text = game_over_font.render("Game Over!", True, RED)
#             restart_text = font.render("Press 'R' to Restart", True, WHITE)
#             screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 50))
#             screen.blit(restart_text, (screen.get_width() // 2 - restart_text.get_width() // 2, screen.get_height() // 2 + 10))

#         pygame.display.flip()
#         clock.tick(30)

import pygame
import random
from constants import GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE, SHAPES, SHAPE_COLORS, WHITE, RED, BLUE, BLACK
from grid import initialize_grid, draw_grid, draw_preview, place_shape_on_grid, clear_full_rows
from utils import rotate_shape, draw_button, check_collision, check_game_over, draw_block

def main():
    global GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE
    pygame.init()

    # Dimensions for the game window and preview pane
    GAME_WIDTH = GRID_WIDTH * BLOCK_SIZE
    GAME_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
    PREVIEW_WIDTH = 200  # Width for the next block preview pane
    WINDOW_WIDTH = GAME_WIDTH + PREVIEW_WIDTH  # Total window width

    # Create the main window
    screen = pygame.display.set_mode((WINDOW_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 72)

    # Initialize grid and game variables
    grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
    BLOCK_SIZE = min(GAME_WIDTH // GRID_WIDTH, GAME_HEIGHT // GRID_HEIGHT)
    current_shape_index = random.randint(0, len(SHAPES) - 1)
    current_shape = SHAPES[current_shape_index]
    current_color = SHAPE_COLORS[current_shape_index]
    next_shape_index = random.randint(0, len(SHAPES) - 1)
    next_shape = SHAPES[next_shape_index]
    next_color = SHAPE_COLORS[next_shape_index]
    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

    normal_tick_rate = 500
    fast_tick_rate = 100
    last_tick = pygame.time.get_ticks()

    horizontal_move_delay = 150
    last_horizontal_move = pygame.time.get_ticks()

    rotation_delay = 200
    last_rotation_time = pygame.time.get_ticks()

    score = 0
    lines_cleared = 0
    level = 0

    game_running = False
    game_paused = False
    game_over = False

    start_button_rect = (50, 10, 100, 50)
    pause_button_rect = (200, 10, 150, 50)

    def calculate_score(lines, level):
        """Calculate score based on lines cleared and level."""
        line_scores = {1: 40, 2: 100, 3: 300, 4: 1200}
        return line_scores.get(lines, 0) * (level + 1)

    while True:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button_rect[0] <= mouse_x <= start_button_rect[0] + start_button_rect[2] and \
                   start_button_rect[1] <= mouse_y <= start_button_rect[1] + start_button_rect[3]:
                    game_running = True
                    game_over = False
                    grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
                    current_shape_index = random.randint(0, len(SHAPES) - 1)
                    current_shape = SHAPES[current_shape_index]
                    current_color = SHAPE_COLORS[current_shape_index]
                    next_shape_index = random.randint(0, len(SHAPES) - 1)
                    next_shape = SHAPES[next_shape_index]
                    next_color = SHAPE_COLORS[next_shape_index]
                    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
                    score = 0
                    lines_cleared = 0
                    level = 0

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:  # Restart the game
                    game_running = True
                    game_over = False
                    grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
                    current_shape_index = random.randint(0, len(SHAPES) - 1)
                    current_shape = SHAPES[current_shape_index]
                    current_color = SHAPE_COLORS[current_shape_index]
                    next_shape_index = random.randint(0, len(SHAPES) - 1)
                    next_shape = SHAPES[next_shape_index]
                    next_color = SHAPE_COLORS[next_shape_index]
                    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
                    score = 0
                    lines_cleared = 0
                    level = 0

        if game_running and not game_paused and not game_over:
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

            # Automatic downward movement
            current_tick_rate = fast_tick_rate if keys[pygame.K_DOWN] else normal_tick_rate
            if current_time - last_tick > current_tick_rate:
                if not check_collision(grid, current_shape, shape_x, shape_y + 1):
                    shape_y += 1
                else:
                    place_shape_on_grid(grid, current_shape, shape_x, shape_y, current_color)
                    cleared_rows = clear_full_rows(grid)
                    if cleared_rows > 0:
                        score += calculate_score(cleared_rows, level)
                        lines_cleared += cleared_rows
                        if lines_cleared // 10 > level:
                            level += 1
                    if check_game_over(grid):
                        game_running = False
                        game_over = True
                    else:
                        current_shape_index = next_shape_index
                        current_shape = next_shape
                        current_color = next_color
                        next_shape_index = random.randint(0, len(SHAPES) - 1)
                        next_shape = SHAPES[next_shape_index]
                        next_color = SHAPE_COLORS[next_shape_index]
                        shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
                last_tick = current_time

        # Clear the screen
        screen.fill(BLACK)

        # Draw the grid and current shape
        draw_grid(screen, grid, BLOCK_SIZE)
        for y, row in enumerate(current_shape):
            for x, value in enumerate(row):
                if value:
                    draw_block(screen, shape_x + x, shape_y + y, current_color, BLOCK_SIZE)

        # Draw the preview pane
        preview_surface = pygame.Surface((PREVIEW_WIDTH, GAME_HEIGHT))
        draw_preview(preview_surface, next_shape, next_color, BLOCK_SIZE)
        screen.blit(preview_surface, (GAME_WIDTH, 0))

        # Display score and level
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        lines_text = font.render(f"Lines: {lines_cleared}", True, WHITE)
        screen.blit(score_text, (10, 50))
        screen.blit(level_text, (10, 80))
        screen.blit(lines_text, (10, 110))

        # Draw buttons
        draw_button(screen, "Start", start_button_rect, font, WHITE, RED)
        draw_button(screen, "Pause" if game_running else "Continue", pause_button_rect, font, WHITE, BLUE)

        if game_over:
            game_over_text = game_over_font.render("Game Over!", True, RED)
            restart_text = font.render("Press 'R' to Restart", True, WHITE)
            screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 50))
            screen.blit(restart_text, (screen.get_width() // 2 - restart_text.get_width() // 2, screen.get_height() // 2 + 10))

        pygame.display.flip()
        clock.tick(30)
