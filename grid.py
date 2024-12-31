# import pygame
# from constants import BLACK, WHITE

# def initialize_grid(width, height):
#     return [[(0, BLACK) for _ in range(width)] for _ in range(height)]

# def draw_grid(screen, grid, block_size):
#     for x in range(0, len(grid[0]) * block_size, block_size):
#         pygame.draw.line(screen, WHITE, (x, 0), (x, len(grid) * block_size))
#     for y in range(0, len(grid) * block_size, block_size):
#         pygame.draw.line(screen, WHITE, (0, y), (len(grid[0]) * block_size, y))

#     for y, row in enumerate(grid):
#         for x, (filled, color) in enumerate(row):
#             if filled:
#                 pygame.draw.rect(screen, color, (x * block_size, y * block_size, block_size, block_size))

# def place_shape_on_grid(grid, shape, x, y, color):
#     """
#     Place a shape on the grid at the specified position (x, y).
#     Handles boundary conditions to avoid out-of-bounds errors.
#     """
#     for dy, row in enumerate(shape):
#         for dx, value in enumerate(row):
#             if value and 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]):
#                 grid[y + dy][x + dx] = (1, color)

# def clear_full_rows(grid):
#     """
#     Check for and clear full rows in the grid.
#     Rows that are fully covered by blocks are removed, 
#     and rows above are shifted downward. Empty rows are added at the top.
#     """
#     full_rows = [y for y, row in enumerate(grid) if all(cell[0] for cell in row)]
#     for row in full_rows:
#         # Remove the full row
#         grid.pop(row)
#         # Insert an empty row at the top
#         grid.insert(0, [(0, BLACK) for _ in range(len(grid[0]))])
#     return len(full_rows)  # Return the number of cleared rows

import pygame
from constants import BLACK, WHITE

def initialize_grid(width, height):
    """Initialize the grid with empty cells."""
    return [[(0, BLACK) for _ in range(width)] for _ in range(height)]

def draw_grid(screen, grid, block_size):
    """Draw the main Tetris grid."""
    for x in range(0, len(grid[0]) * block_size, block_size):
        pygame.draw.line(screen, WHITE, (x, 0), (x, len(grid) * block_size))
    for y in range(0, len(grid) * block_size, block_size):
        pygame.draw.line(screen, WHITE, (0, y), (len(grid[0]) * block_size, y))

    for y, row in enumerate(grid):
        for x, (filled, color) in enumerate(row):
            if filled:
                pygame.draw.rect(screen, color, (x * block_size, y * block_size, block_size, block_size))

def draw_preview(surface, shape, color, block_size):
    """Draw the next shape in the preview pane."""
    surface.fill(BLACK)  # Clear the preview pane
    start_x = surface.get_width() // 2 - (len(shape[0]) * block_size) // 2
    start_y = surface.get_height() // 2 - (len(shape) * block_size) // 2
    for y, row in enumerate(shape):
        for x, value in enumerate(row):
            if value:
                pygame.draw.rect(surface, color, (start_x + x * block_size, start_y + y * block_size, block_size, block_size))
                pygame.draw.rect(surface, WHITE, (start_x + x * block_size, start_y + y * block_size, block_size, block_size), 1)

def place_shape_on_grid(grid, shape, x, y, color):
    """Place a shape on the grid at the specified position (x, y)."""
    for dy, row in enumerate(shape):
        for dx, value in enumerate(row):
            if value and 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]):
                grid[y + dy][x + dx] = (1, color)

def clear_full_rows(grid):
    """Check for and clear full rows in the grid."""
    full_rows = [y for y, row in enumerate(grid) if all(cell[0] for cell in row)]
    for row in full_rows:
        grid.pop(row)
        grid.insert(0, [(0, BLACK) for _ in range(len(grid[0]))])
    return len(full_rows)  # Return the number of cleared rows