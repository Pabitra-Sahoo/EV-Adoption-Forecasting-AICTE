const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreDisplay = document.getElementById('score');

const gridSize = 6;
const dotRadius = 5;
const dotDistance = 60;
let dots = [];
let lines = [];
let boxes = [];
let currentPlayer = 1;
let scores = { 1: 0, 2: 0 };

function init() {
    for (let row = 0; row < gridSize; row++) {
        dots[row] = [];
        for (let col = 0; col < gridSize; col++) {
            dots[row][col] = {
                x: col * dotDistance + dotDistance,
                y: row * dotDistance + dotDistance,
                connections: []
            };
        }
    }
    drawBoard();
}

function drawBoard() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let row = 0; row < gridSize; row++) {
        for (let col = 0; col < gridSize; col++) {
            drawDot(dots[row][col]);
        }
    }
    for (const line of lines) {
        drawLine(line);
    }
    for (const box of boxes) {
        drawBox(box);
    }
}

function drawDot(dot) {
    ctx.beginPath();
    ctx.arc(dot.x, dot.y, dotRadius, 0, Math.PI * 2);
    ctx.fillStyle = 'black';
    ctx.fill();
}

function drawLine(line) {
    ctx.beginPath();
    ctx.moveTo(line.from.x, line.from.y);
    ctx.lineTo(line.to.x, line.to.y);
    ctx.strokeStyle = line.player === 1 ? 'blue' : 'red';
    ctx.lineWidth = 2;
    ctx.stroke();
}

function drawBox(box) {
    ctx.fillStyle = box.player === 1 ? 'rgba(0, 0, 255, 0.2)' : 'rgba(255, 0, 0, 0.2)';
    ctx.fillRect(box.x, box.y, dotDistance, dotDistance);
}

function getClickedDot(x, y) {
    for (let row = 0; row < gridSize; row++) {
        for (let col = 0; col < gridSize; col++) {
            const dot = dots[row][col];
            const distance = Math.sqrt((x - dot.x) ** 2 + (y - dot.y) ** 2);
            if (distance < dotRadius) {
                return dot;
            }
        }
    }
    return null;
}

function isLineAlreadyDrawn(dot1, dot2) {
    for (const line of lines) {
        if ((line.from === dot1 && line.to === dot2) || (line.from === dot2 && line.to === dot1)) {
            return true;
        }
    }
    return false;
}

function checkForBoxClosure(dot1, dot2) {
    const row1 = dots.findIndex(row => row.includes(dot1));
    const col1 = dots[row1].findIndex(dot => dot === dot1);
    const row2 = dots.findIndex(row => row.includes(dot2));
    const col2 = dots[row2].findIndex(dot => dot === dot2);

    if (Math.abs(row1 - row2) + Math.abs(col1 - col2) !== 1) {
        return false;
    }

    let boxesClosed = 0;
    if (row1 === row2) {
        const minCol = Math.min(col1, col2);
        const maxCol = Math.max(col1, col2);
        if (row1 > 0) {
            const topLeft = dots[row1 - 1][minCol];
            const topRight = dots[row1 - 1][maxCol];
            if (isLineAlreadyDrawn(topLeft, topRight) &&
                isLineAlreadyDrawn(topLeft, dot1) &&
                isLineAlreadyDrawn(topRight, dot2)) {
                boxes.push({ x: topLeft.x, y: topLeft.y, player: currentPlayer });
                boxesClosed++;
            }
        }
        if (row1 < gridSize - 1) {
            const bottomLeft = dots[row1 + 1][minCol];
            const bottomRight = dots[row1 + 1][maxCol];
             if (isLineAlreadyDrawn(bottomLeft, bottomRight) &&
                isLineAlreadyDrawn(bottomLeft, dot1) &&
                isLineAlreadyDrawn(bottomRight, dot2)) {
                boxes.push({ x: dot1.x, y: dot1.y, player: currentPlayer });
                boxesClosed++;
            }
        }
    } else {
        const minRow = Math.min(row1, row2);
        const maxRow = Math.max(row1, row2);
        if (col1 > 0) {
            const topLeft = dots[minRow][col1 - 1];
            const bottomLeft = dots[maxRow][col1 - 1];
            if (isLineAlreadyDrawn(topLeft, bottomLeft) &&
                isLineAlreadyDrawn(topLeft, dot1) &&
                isLineAlreadyDrawn(bottomLeft, dot2)) {
                 boxes.push({ x: topLeft.x, y: topLeft.y, player: currentPlayer });
                boxesClosed++;
            }
        }
        if (col1 < gridSize - 1) {
            const topRight = dots[minRow][col1 + 1];
            const bottomRight = dots[maxRow][col1 + 1];
             if (isLineAlreadyDrawn(topRight, bottomRight) &&
                isLineAlreadyDrawn(topRight, dot1) &&
                isLineAlreadyDrawn(bottomRight, dot2)) {
                boxes.push({ x: dot1.x, y: dot1.y, player: currentPlayer });
                boxesClosed++;
            }
        }
    }
    return boxesClosed;
}

function updateScore() {
    scoreDisplay.textContent = `Player 1: ${scores[1]}, Player 2: ${scores[2]}`;
}

canvas.addEventListener('click', (event) => {
    const x = event.offsetX;
    const y = event.offsetY;
    const clickedDot = getClickedDot(x, y);

    if (clickedDot) {
        if (!firstDot) {
            firstDot = clickedDot;
        } else if (clickedDot !== firstDot && !isLineAlreadyDrawn(firstDot, clickedDot)) {
            lines.push({ from: firstDot, to: clickedDot, player: currentPlayer });
            const boxesClosed = checkForBoxClosure(firstDot, clickedDot);
            scores[currentPlayer] += boxesClosed;
            updateScore();
            if (boxesClosed === 0) {
                currentPlayer = currentPlayer === 1 ? 2 : 1;
            }
            firstDot = null;
            drawBoard();
        } else {
            firstDot = clickedDot;
        }
    }
});

let firstDot = null;
init();
updateScore();
