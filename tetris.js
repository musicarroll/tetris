// // Constants
// const canvas = document.getElementById("gameCanvas");
// const ctx = canvas.getContext("2d");
// const SCREEN_WIDTH = 400;
// const SCREEN_HEIGHT = 500;
// const BLOCK_SIZE = 25;
// const GRID_WIDTH = SCREEN_WIDTH / BLOCK_SIZE;
// const GRID_HEIGHT = SCREEN_HEIGHT / BLOCK_SIZE;
// canvas.width = SCREEN_WIDTH;
// canvas.height = SCREEN_HEIGHT;

// // Colors and Shapes
// const COLORS = {
//     0: "#00FFFF", // Cyan (I)
//     1: "#FFFF00", // Yellow (O)
//     2: "#FF00FF", // Magenta (T)
//     3: "#0000FF", // Blue (J)
//     4: "#FFA500", // Orange (L)
//     5: "#00FF00", // Green (S)
//     6: "#FF0000", // Red (Z)
//     empty: "#000000", // Black (grid background)
// };
// const SHAPES = [
//     [[1, 1, 1, 1]], // I
//     [[1, 1], [1, 1]], // O
//     [[1, 1, 1], [0, 1, 0]], // T
//     [[1, 1, 1], [0, 0, 1]], // J
//     [[1, 1, 1], [1, 0, 0]], // L
//     [[0, 1, 1], [1, 1, 0]], // S
//     [[1, 1, 0], [0, 1, 1]], // Z
// ];

// // Game Variables
// let grid, currentShape, currentColor, shapeX, shapeY, nextShape, nextColor;
// let score = 0, level = 0, linesCleared = 0;
// let gameRunning = false, gamePaused = false;
// let lastTick = 0, normalTickRate = 1000, fastTickRate = 100;
// let isFastDropping = false; // Tracks if down arrow is held

// // Initialize Grid
// function initializeGrid() {
//     return Array.from({ length: GRID_HEIGHT }, () => Array(GRID_WIDTH).fill(0));
// }

// // Draw Grid
// function drawGrid() {
//     ctx.fillStyle = COLORS.empty;
//     ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
//     for (let y = 0; y < GRID_HEIGHT; y++) {
//         for (let x = 0; x < GRID_WIDTH; x++) {
//             if (grid[y][x]) {
//                 ctx.fillStyle = COLORS[grid[y][x]];
//                 ctx.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
//                 ctx.strokeStyle = "#FFF";
//                 ctx.strokeRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
//             }
//         }
//     }
// }

// // Draw Shape
// function drawShape(shape, color, offsetX, offsetY) {
//     ctx.fillStyle = color;
//     for (let y = 0; y < shape.length; y++) {
//         for (let x = 0; x < shape[y].length; x++) {
//             if (shape[y][x]) {
//                 ctx.fillRect(
//                     (shapeX + x + offsetX) * BLOCK_SIZE,
//                     (shapeY + y + offsetY) * BLOCK_SIZE,
//                     BLOCK_SIZE,
//                     BLOCK_SIZE
//                 );
//                 ctx.strokeStyle = "#FFF";
//                 ctx.strokeRect(
//                     (shapeX + x + offsetX) * BLOCK_SIZE,
//                     (shapeY + y + offsetY) * BLOCK_SIZE,
//                     BLOCK_SIZE,
//                     BLOCK_SIZE
//                 );
//             }
//         }
//     }
// }

// // Rotate Shape
// function rotateShape(shape) {
//     return shape[0].map((_, colIndex) => shape.map(row => row[colIndex]).reverse());
// }

// // Check Collision
// function checkCollision(shape, offsetX, offsetY) {
//     for (let y = 0; y < shape.length; y++) {
//         for (let x = 0; x < shape[y].length; x++) {
//             if (
//                 shape[y][x] &&
//                 (shapeY + y + offsetY >= GRID_HEIGHT || // Bottom boundary
//                     shapeX + x + offsetX < 0 || // Left boundary
//                     shapeX + x + offsetX >= GRID_WIDTH || // Right boundary
//                     grid[shapeY + y + offsetY]?.[shapeX + x + offsetX]) // Occupied space
//             ) {
//                 return true;
//             }
//         }
//     }
//     return false;
// }

// // Place Shape on Grid
// function placeShapeOnGrid(shape, color) {
//     for (let y = 0; y < shape.length; y++) {
//         for (let x = 0; x < shape[y].length; x++) {
//             if (shape[y][x]) {
//                 grid[shapeY + y][shapeX + x] = Object.keys(COLORS).find(key => COLORS[key] === color);
//             }
//         }
//     }
// }

// // Clear Full Rows
// function clearFullRows() {
//     let clearedRows = 0;
//     for (let y = GRID_HEIGHT - 1; y >= 0; y--) {
//         if (grid[y].every(cell => cell !== 0)) {
//             grid.splice(y, 1);
//             grid.unshift(Array(GRID_WIDTH).fill(0));
//             clearedRows++;
//             y++;
//         }
//     }
//     return clearedRows;
// }

// // Calculate Score
// function calculateScore(lines, level) {
//     const lineScores = { 1: 40, 2: 100, 3: 300, 4: 1200 };
//     return (lineScores[lines] || 0) * (level + 1);
// }

// // Spawn New Shape
// function spawnShape() {
//     const shapeIndex = Math.floor(Math.random() * SHAPES.length);
//     currentShape = SHAPES[shapeIndex];
//     currentColor = COLORS[shapeIndex];
//     nextShape = SHAPES[Math.floor(Math.random() * SHAPES.length)];
//     nextColor = COLORS[Object.keys(COLORS).find(key => COLORS[key] === nextShape)];
//     shapeX = Math.floor((GRID_WIDTH - currentShape[0].length) / 2);
//     shapeY = 0;

//     if (checkCollision(currentShape, 0, 0)) {
//         gameRunning = false; // Game over
//     }
// }

// // Game Loop
// function gameLoop(timestamp) {
//     if (!gameRunning || gamePaused) return;

//     const tickRate = isFastDropping ? fastTickRate : normalTickRate;
//     if (timestamp - lastTick >= tickRate) {
//         if (!checkCollision(currentShape, 0, 1)) {
//             shapeY++;
//         } else {
//             placeShapeOnGrid(currentShape, currentColor);
//             const clearedRows = clearFullRows();
//             if (clearedRows > 0) {
//                 score += calculateScore(clearedRows, level);
//                 linesCleared += clearedRows;
//                 if (linesCleared % 10 === 0) level++;
//             }
//             spawnShape();
//         }
//         lastTick = timestamp;
//     }

//     drawGrid();
//     drawShape(currentShape, currentColor, 0, 0);
//     requestAnimationFrame(gameLoop);
// }

// // Start Game
// document.getElementById("startButton").addEventListener("click", () => {
//     grid = initializeGrid();
//     spawnShape();
//     gameRunning = true;
//     gamePaused = false;
//     score = 0;
//     level = 0;
//     linesCleared = 0;
//     requestAnimationFrame(gameLoop);
// });

// // Pause Game
// document.getElementById("pauseButton").addEventListener("click", () => {
//     gamePaused = !gamePaused;
//     if (!gamePaused) requestAnimationFrame(gameLoop);
// });

// // Handle Keyboard Input
// document.addEventListener("keydown", (event) => {
//     if (!gameRunning || gamePaused) return;

//     if (event.key === "ArrowLeft" && !checkCollision(currentShape, -1, 0)) {
//         shapeX--;
//     } else if (event.key === "ArrowRight" && !checkCollision(currentShape, 1, 0)) {
//         shapeX++;
//     } else if (event.key === "ArrowDown") {
//         isFastDropping = true;
//     } else if (event.key === "ArrowUp") {
//         const rotatedShape = rotateShape(currentShape);
//         if (!checkCollision(rotatedShape, 0, 0)) {
//             currentShape = rotatedShape;
//         }
//     }
// });

// // Handle Key Release for Down Arrow
// document.addEventListener("keyup", (event) => {
//     if (event.key === "ArrowDown") {
//         isFastDropping = false;
//     }
// });

// Constants
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const SCREEN_WIDTH = 400;
const SCREEN_HEIGHT = 500;
const BLOCK_SIZE = 25;
const GRID_WIDTH = SCREEN_WIDTH / BLOCK_SIZE;
const GRID_HEIGHT = SCREEN_HEIGHT / BLOCK_SIZE;
canvas.width = SCREEN_WIDTH;
canvas.height = SCREEN_HEIGHT;

// Colors and Shapes
const COLORS = {
    0: "#00FFFF", // Cyan (I)
    1: "#FFFF00", // Yellow (O)
    2: "#FF00FF", // Magenta (T)
    3: "#0000FF", // Blue (J)
    4: "#FFA500", // Orange (L)
    5: "#00FF00", // Green (S)
    6: "#FF0000", // Red (Z)
    empty: "#000000", // Black (grid background)
};
const SHAPES = [
    [[1, 1, 1, 1]], // I
    [[1, 1], [1, 1]], // O
    [[1, 1, 1], [0, 1, 0]], // T
    [[1, 1, 1], [0, 0, 1]], // J
    [[1, 1, 1], [1, 0, 0]], // L
    [[0, 1, 1], [1, 1, 0]], // S
    [[1, 1, 0], [0, 1, 1]], // Z
];

// Game Variables
let grid, currentShape, currentColor, shapeX, shapeY, nextShape, nextColor;
let score = 0, level = 0, linesCleared = 0;
let gameRunning = false, gamePaused = false;
let lastTick = 0, normalTickRate = 1000, fastTickRate = 100;
let isFastDropping = false; // Tracks if down arrow is held

// DOM Elements
const scoreElement = document.getElementById("score");
const levelElement = document.getElementById("level");
const linesElement = document.getElementById("lines");

// Initialize Grid
function initializeGrid() {
    return Array.from({ length: GRID_HEIGHT }, () => Array(GRID_WIDTH).fill(0));
}

// Draw Grid
function drawGrid() {
    ctx.fillStyle = COLORS.empty;
    ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
    for (let y = 0; y < GRID_HEIGHT; y++) {
        for (let x = 0; x < GRID_WIDTH; x++) {
            if (grid[y][x]) {
                ctx.fillStyle = COLORS[grid[y][x]];
                ctx.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
                ctx.strokeStyle = "#FFF";
                ctx.strokeRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
            }
        }
    }
}

// Draw Shape
function drawShape(shape, color, offsetX, offsetY) {
    ctx.fillStyle = color;
    for (let y = 0; y < shape.length; y++) {
        for (let x = 0; x < shape[y].length; x++) {
            if (shape[y][x]) {
                ctx.fillRect(
                    (shapeX + x + offsetX) * BLOCK_SIZE,
                    (shapeY + y + offsetY) * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                );
                ctx.strokeStyle = "#FFF";
                ctx.strokeRect(
                    (shapeX + x + offsetX) * BLOCK_SIZE,
                    (shapeY + y + offsetY) * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                );
            }
        }
    }
}

// Rotate Shape
function rotateShape(shape) {
    return shape[0].map((_, colIndex) => shape.map(row => row[colIndex]).reverse());
}

// Check Collision
function checkCollision(shape, offsetX, offsetY) {
    for (let y = 0; y < shape.length; y++) {
        for (let x = 0; x < shape[y].length; x++) {
            if (
                shape[y][x] &&
                (shapeY + y + offsetY >= GRID_HEIGHT || // Bottom boundary
                    shapeX + x + offsetX < 0 || // Left boundary
                    shapeX + x + offsetX >= GRID_WIDTH || // Right boundary
                    grid[shapeY + y + offsetY]?.[shapeX + x + offsetX]) // Occupied space
            ) {
                return true;
            }
        }
    }
    return false;
}

// Place Shape on Grid
function placeShapeOnGrid(shape, color) {
    for (let y = 0; y < shape.length; y++) {
        for (let x = 0; x < shape[y].length; x++) {
            if (shape[y][x]) {
                grid[shapeY + y][shapeX + x] = Object.keys(COLORS).find(key => COLORS[key] === color);
            }
        }
    }
}

// Clear Full Rows
function clearFullRows() {
    let clearedRows = 0;
    for (let y = GRID_HEIGHT - 1; y >= 0; y--) {
        if (grid[y].every(cell => cell !== 0)) {
            grid.splice(y, 1);
            grid.unshift(Array(GRID_WIDTH).fill(0));
            clearedRows++;
            y++;
        }
    }
    return clearedRows;
}

// Calculate Score
function calculateScore(lines, level) {
    const lineScores = { 1: 40, 2: 100, 3: 300, 4: 1200 };
    return (lineScores[lines] || 0) * (level + 1);
}

// Update UI
function updateUI() {
    scoreElement.textContent = score;
    levelElement.textContent = level;
    linesElement.textContent = linesCleared;
}

// Spawn New Shape
function spawnShape() {
    const shapeIndex = Math.floor(Math.random() * SHAPES.length);
    currentShape = SHAPES[shapeIndex];
    currentColor = COLORS[shapeIndex];
    nextShape = SHAPES[Math.floor(Math.random() * SHAPES.length)];
    nextColor = COLORS[Object.keys(COLORS).find(key => COLORS[key] === nextShape)];
    shapeX = Math.floor((GRID_WIDTH - currentShape[0].length) / 2);
    shapeY = 0;

    if (checkCollision(currentShape, 0, 0)) {
        gameRunning = false; // Game over
    }
}

// Game Loop
function gameLoop(timestamp) {
    if (!gameRunning || gamePaused) return;

    const tickRate = isFastDropping ? fastTickRate : normalTickRate;
    if (timestamp - lastTick >= tickRate) {
        if (!checkCollision(currentShape, 0, 1)) {
            shapeY++;
        } else {
            placeShapeOnGrid(currentShape, currentColor);
            const clearedRows = clearFullRows();
            if (clearedRows > 0) {
                score += calculateScore(clearedRows, level);
                linesCleared += clearedRows;
                if (linesCleared % 10 === 0) level++;
                updateUI(); // Update UI after scoring
            }
            spawnShape();
        }
        lastTick = timestamp;
    }

    drawGrid();
    drawShape(currentShape, currentColor, 0, 0);
    requestAnimationFrame(gameLoop);
}

// Start Game
document.getElementById("startButton").addEventListener("click", () => {
    grid = initializeGrid();
    spawnShape();
    gameRunning = true;
    gamePaused = false;
    score = 0;
    level = 0;
    linesCleared = 0;
    updateUI(); // Reset UI
    requestAnimationFrame(gameLoop);
});

// Pause Game
document.getElementById("pauseButton").addEventListener("click", () => {
    gamePaused = !gamePaused;
    if (!gamePaused) requestAnimationFrame(gameLoop);
});

// Handle Keyboard Input
document.addEventListener("keydown", (event) => {
    if (!gameRunning || gamePaused) return;

    if (event.key === "ArrowLeft" && !checkCollision(currentShape, -1, 0)) {
        shapeX--;
    } else if (event.key === "ArrowRight" && !checkCollision(currentShape, 1, 0)) {
        shapeX++;
    } else if (event.key === "ArrowDown") {
        isFastDropping = true;
    } else if (event.key === "ArrowUp") {
        const rotatedShape = rotateShape(currentShape);
        if (!checkCollision(rotatedShape, 0, 0)) {
            currentShape = rotatedShape;
        }
    }
});

// Handle Key Release for Down Arrow
document.addEventListener("keyup", (event) => {
    if (event.key === "ArrowDown") {
        isFastDropping = false;
    }
});

// DOM Elements for new buttons
const rotateButton = document.getElementById("rotateButton");
const speedupButton = document.getElementById("speedupButton");
const leftButton = document.getElementById("leftButton");
const rightButton = document.getElementById("rightButton");

// Handle Button Controls
rotateButton.addEventListener("click", () => {
    if (gameRunning && !gamePaused) {
        const rotatedShape = rotateShape(currentShape);
        if (!checkCollision(rotatedShape, 0, 0)) {
            currentShape = rotatedShape;
        }
    }
});

speedupButton.addEventListener("mousedown", () => {
    if (gameRunning && !gamePaused) {
        isFastDropping = true;
    }
});

speedupButton.addEventListener("mouseup", () => {
    isFastDropping = false;
});

leftButton.addEventListener("click", () => {
    if (gameRunning && !gamePaused && !checkCollision(currentShape, -1, 0)) {
        shapeX--;
    }
});

rightButton.addEventListener("click", () => {
    if (gameRunning && !gamePaused && !checkCollision(currentShape, 1, 0)) {
        shapeX++;
    }
});
