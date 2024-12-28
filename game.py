import pygame
import random
from constants import GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE, SHAPES, WHITE, RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE, BLACK
from grid import initialize_grid, draw_grid, place_shape_on_grid, clear_full_rows
from utils import rotate_shape, draw_button, check_collision, check_game_over, draw_block  # Import draw_block



# def main():
#     global GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE  # Allow global modification of these variables
#     pygame.init()
#     screen = pygame.display.set_mode((GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), pygame.RESIZABLE)
#     pygame.display.set_caption("Tetris")
#     clock = pygame.time.Clock()

#     font = pygame.font.Font(None, 36)

#     # Initialize grid and game variables
#     BLOCK_SIZE = min(screen.get_width() // GRID_WIDTH, screen.get_height() // GRID_HEIGHT)
#     grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
#     current_shape = random.choice(SHAPES)
#     current_color = random.choice([RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE])
#     shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

#     # Timing variables for block descent and input handling
#     normal_tick_rate = 500  # milliseconds for regular descent
#     fast_tick_rate = 100    # milliseconds for faster descent
#     last_tick = pygame.time.get_ticks()

#     horizontal_move_delay = 150  # milliseconds delay for horizontal movement
#     last_horizontal_move = pygame.time.get_ticks()

#     rotation_delay = 200  # milliseconds delay for rotation
#     last_rotation_time = pygame.time.get_ticks()

#     game_running = False  # Game is initially not running
#     game_paused = False   # Game is initially not paused

#     start_button_rect = (50, 10, 100, 50)  # Position and size for Start button
#     pause_button_rect = (200, 10, 150, 50)  # Position and size for Pause/Continue button

#     while True:
#         current_time = pygame.time.get_ticks()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#             # Handle window resize events
#             if event.type == pygame.VIDEORESIZE:
#                 window_width, window_height = event.w, event.h
#                 screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

#                 # Dynamically update BLOCK_SIZE to maintain constant grid dimensions
#                 new_block_size = min(window_width // GRID_WIDTH, window_height // GRID_HEIGHT)
#                 scaling_factor = new_block_size / BLOCK_SIZE
#                 BLOCK_SIZE = new_block_size

#                 # Reinitialize the grid with the updated BLOCK_SIZE
#                 grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)

#                 # Scale and validate current shape position
#                 shape_x = max(0, min(GRID_WIDTH - len(current_shape[0]), int(shape_x * scaling_factor)))
#                 shape_y = max(0, min(GRID_HEIGHT - len(current_shape), int(shape_y * scaling_factor)))

#             # Handle mouse clicks for buttons
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = event.pos
#                 if start_button_rect[0] <= mouse_x <= start_button_rect[0] + start_button_rect[2] and \
#                    start_button_rect[1] <= mouse_y <= start_button_rect[1] + start_button_rect[3]:
#                     game_running = True
#                 if pause_button_rect[0] <= mouse_x <= pause_button_rect[0] + pause_button_rect[2] and \
#                    pause_button_rect[1] <= mouse_y <= pause_button_rect[1] + pause_button_rect[3] and game_running:
#                     game_paused = not game_paused

#         if game_running and not game_paused:
#             # Game logic when running and not paused
#             keys = pygame.key.get_pressed()

#             # Handle horizontal movement with delay
#             if current_time - last_horizontal_move > horizontal_move_delay:
#                 if keys[pygame.K_LEFT] and not check_collision(grid, current_shape, shape_x - 1, shape_y):
#                     shape_x -= 1
#                     last_horizontal_move = current_time
#                 if keys[pygame.K_RIGHT] and not check_collision(grid, current_shape, shape_x + 1, shape_y):
#                     shape_x += 1
#                     last_horizontal_move = current_time

#             # Handle rotation with delay
#             if keys[pygame.K_UP] and current_time - last_rotation_time > rotation_delay:
#                 rotated = rotate_shape(current_shape)
#                 if not check_collision(grid, rotated, shape_x, shape_y):
#                     current_shape = rotated
#                     last_rotation_time = current_time

#             # Determine descent rate based on whether the down arrow is pressed
#             current_tick_rate = fast_tick_rate if keys[pygame.K_DOWN] else normal_tick_rate

#             # Handle automatic downward movement
#             if current_time - last_tick > current_tick_rate:
#                 if not check_collision(grid, current_shape, shape_x, shape_y + 1):
#                     shape_y += 1
#                 else:
#                     place_shape_on_grid(grid, current_shape, shape_x, shape_y, current_color)
                    
#                     # Check for and clear full rows
#                     cleared_rows = clear_full_rows(grid)
#                     if cleared_rows > 0:
#                         print(f"Cleared {cleared_rows} row(s)!")

#                     # Check for game over condition
#                     if check_game_over(grid):
#                         game_running = False
#                     else:
#                         # Spawn a new shape
#                         shape_y = 0
#                         shape_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
#                         current_shape = random.choice(SHAPES)
#                         current_color = random.choice([RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE])
#                 last_tick = current_time

#         # Draw everything
#         screen.fill(BLACK)

#         # Draw buttons
#         draw_button(screen, "Start", start_button_rect, font, WHITE, RED)
#         draw_button(screen, "Pause" if game_running and not game_paused else "Continue",
#                     pause_button_rect, font, WHITE, BLUE)

#         # Draw grid and blocks only if the game is running
#         if game_running:
#             draw_grid(screen, grid, BLOCK_SIZE)
#             for y, row in enumerate(current_shape):
#                 for x, value in enumerate(row):
#                     if value:
#                         draw_block(screen, shape_x + x, shape_y + y, current_color, BLOCK_SIZE)

#         pygame.display.flip()
#         clock.tick(30)

def main():
    global GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), pygame.RESIZABLE)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 72)

    # Initialize grid and game variables
    BLOCK_SIZE = min(screen.get_width() // GRID_WIDTH, screen.get_height() // GRID_HEIGHT)
    grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
    current_shape = random.choice(SHAPES)
    current_color = random.choice([RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE])
    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

    normal_tick_rate = 500
    fast_tick_rate = 100
    last_tick = pygame.time.get_ticks()

    horizontal_move_delay = 150
    last_horizontal_move = pygame.time.get_ticks()

    rotation_delay = 200
    last_rotation_time = pygame.time.get_ticks()

    game_running = False
    game_paused = False
    game_over = False  # New variable for game over state

    start_button_rect = (50, 10, 100, 50)
    pause_button_rect = (200, 10, 150, 50)

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
                    grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)  # Reset grid
                    current_shape = random.choice(SHAPES)  # Reset shape
                    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

                if pause_button_rect[0] <= mouse_x <= pause_button_rect[0] + pause_button_rect[2] and \
                   pause_button_rect[1] <= mouse_y <= pause_button_rect[1] + pause_button_rect[3] and game_running:
                    game_paused = not game_paused

            # Restart game on key press when game is over
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:  # Restart the game
                    game_running = True
                    game_over = False
                    grid = initialize_grid(GRID_WIDTH, GRID_HEIGHT)
                    current_shape = random.choice(SHAPES)
                    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

        if game_running and not game_paused and not game_over:
            keys = pygame.key.get_pressed()
            if current_time - last_horizontal_move > horizontal_move_delay:
                if keys[pygame.K_LEFT] and not check_collision(grid, current_shape, shape_x - 1, shape_y):
                    shape_x -= 1
                    last_horizontal_move = current_time
                if keys[pygame.K_RIGHT] and not check_collision(grid, current_shape, shape_x + 1, shape_y):
                    shape_x += 1
                    last_horizontal_move = current_time

            if keys[pygame.K_UP] and current_time - last_rotation_time > rotation_delay:
                rotated = rotate_shape(current_shape)
                if not check_collision(grid, rotated, shape_x, shape_y):
                    current_shape = rotated
                    last_rotation_time = current_time

            current_tick_rate = fast_tick_rate if keys[pygame.K_DOWN] else normal_tick_rate
            if current_time - last_tick > current_tick_rate:
                if not check_collision(grid, current_shape, shape_x, shape_y + 1):
                    shape_y += 1
                else:
                    place_shape_on_grid(grid, current_shape, shape_x, shape_y, current_color)
                    cleared_rows = clear_full_rows(grid)
                    if check_game_over(grid):
                        game_running = False
                        game_over = True
                    else:
                        shape_y = 0
                        shape_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
                        current_shape = random.choice(SHAPES)
                        current_color = random.choice([RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE])
                last_tick = current_time

        screen.fill(BLACK)

        draw_button(screen, "Start", start_button_rect, font, WHITE, RED)
        draw_button(screen, "Pause" if game_running and not game_paused else "Continue",
                    pause_button_rect, font, WHITE, BLUE)

        if game_running:
            draw_grid(screen, grid, BLOCK_SIZE)
            for y, row in enumerate(current_shape):
                for x, value in enumerate(row):
                    if value:
                        draw_block(screen, shape_x + x, shape_y + y, current_color, BLOCK_SIZE)

        if game_over:
            game_over_text = game_over_font.render("Game Over!", True, RED)
            restart_text = font.render("Press 'R' to Restart", True, WHITE)
            screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 50))
            screen.blit(restart_text, (screen.get_width() // 2 - restart_text.get_width() // 2, screen.get_height() // 2 + 10))

        pygame.display.flip()
        clock.tick(30)
