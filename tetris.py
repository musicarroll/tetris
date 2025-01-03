import pygame
import random
# This is the original, single file version of the game.
# It is now obsolete.
# It has been refactored into several modules that are imported into main.py.
# So, to launch the game, enter the command python main.py

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 500
BLOCK_SIZE = 25
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Shapes
# Each shape is represented as a list of lists, where 1 indicates a filled block and 0 indicates an empty space
SHAPES = [
    # I Shape (Straight)
    [[1, 1, 1, 1]],
    
    # O Shape (Square)
    [[1, 1],
     [1, 1]],
    
    # T Shape (Tee)
    [[1, 1, 1],
     [0, 1, 0]],
    
    # J Shape (Left L)
    [[1, 1, 1],
     [1, 0, 0]],
    
    # L Shape (Right L)
    [[1, 1, 1],
     [0, 0, 1]],
    
    # S Shape (Left S)
    [[1, 1, 0],
     [0, 1, 1]],
    
    # Z Shape (Right Z)
    [[0, 1, 1],
     [1, 1, 0]]
]

# Initialize game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Function to draw the grid lines
def draw_grid(grid):
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

    for y, row in enumerate(grid):
        for x, (filled, color) in enumerate(row):
            if filled:
                draw_block(x, y, color)

# Function to draw a single block
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Function to rotate a shape clockwise
def rotate_shape(shape):
    return list(zip(*reversed(shape)))

# Function to place a shape on the grid
def place_shape_on_grid(grid, shape, x, y, color):
    for dy, row in enumerate(shape):
        for dx, value in enumerate(row):
            if value:
                grid[y + dy][x + dx] = (1, color)

# Function to check for collision with the walls or other blocks
def check_collision(grid, shape, x, y):
    for dy, row in enumerate(shape):
        for dx, value in enumerate(row):
            if value and (x + dx < 0 or x + dx >= GRID_WIDTH or y + dy >= GRID_HEIGHT or grid[y + dy][x + dx][0]):
                return True
    return False

# Function to check if the game is over
def check_game_over(grid):
    return any(grid[0][x][0] for x in range(GRID_WIDTH))

def main():
    # Initialize the grid with black color
    grid = [[(0, BLACK) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    
    # Select a random shape and color for the current falling shape
    current_shape = random.choice(SHAPES)
    current_color = random.choice([RED, CYAN, YELLOW, MAGENTA, GREEN, BLUE])
    
    # Initial position of the falling shape
    shape_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
    shape_y = 0

    game_over = False

        # Timing variables
    normal_tick_rate = 500  # milliseconds for regular descent
    fast_tick_rate = 100    # milliseconds for faster descent
    last_tick = pygame.time.get_ticks()

    horizontal_move_delay = 150  # milliseconds delay for horizontal movement
    last_horizontal_move = pygame.time.get_ticks()

    rotation_delay = 200  # milliseconds delay for rotation
    last_rotation_time = pygame.time.get_ticks()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # Handle horizontal movement with delay
        current_time = pygame.time.get_ticks()
        if current_time - last_horizontal_move > horizontal_move_delay:
            if keys[pygame.K_LEFT] and shape_x > 0 and not check_collision(grid, current_shape, shape_x - 1, shape_y):
                shape_x -= 1
                last_horizontal_move = current_time
            if keys[pygame.K_RIGHT] and shape_x + len(current_shape[0]) < GRID_WIDTH and not check_collision(grid, current_shape, shape_x + 1, shape_y):
                shape_x += 1
                last_horizontal_move = current_time

        # Handle rotation with delay
        if keys[pygame.K_UP] and current_time - last_rotation_time > rotation_delay:
            rotated_shape = rotate_shape(current_shape)
            if shape_x + len(rotated_shape[0]) <= GRID_WIDTH and shape_y + len(rotated_shape) <= GRID_HEIGHT \
                    and not check_collision(grid, rotated_shape, shape_x, shape_y):
                current_shape = rotated_shape
                last_rotation_time = current_time

        # Determine the descent rate
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
        draw_grid(grid)

        # Draw current shape
        for y, row in enumerate(current_shape):
            for x, value in enumerate(row):
                if value:
                    draw_block(shape_x + x, shape_y + y, current_color)

        pygame.display.flip()
        clock.tick(30)

    # Display "Game Over" message
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 18))
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == "__main__":
    main()
