

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
ORANGE = (255, 165, 0)


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
     [0, 0, 1]],
    
    # L Shape (Right L)
    [[1, 1, 1],
     [1, 0, 0]],
    
    # S Shape (Left S)
    [[0, 1, 1],
     [1, 1, 0]],
    
    # Z Shape (Right Z)
    [[1, 1, 0],
     [0, 1, 1]]
]

# Shape Colors
SHAPE_COLORS = {
    0: CYAN,    # I Shape
    1: YELLOW,  # O Shape
    2: MAGENTA, # T Shape
    3: BLUE,    # J Shape
    4: ORANGE,  # L Shape
    5: GREEN,   # S Shape
    6: RED      # Z Shape
}
