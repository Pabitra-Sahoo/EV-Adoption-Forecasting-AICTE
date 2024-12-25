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
    ctx.fillStyle = 'orange';
    ctx.fill();
}

function drawLine(line) {
    ctx.beginPath();
    ctx.moveTo(line.from.x, line.from.y);
    ctx.lineTo(line.to.x, line.to.y);
    ctx.strokeStyle = line.player === 1 ? 'blue' : 'red';
    ctx.lineWidth = 2;
    ctx.stroke();
    // Line animation
    ctx.strokeStyle = line.player === 1 ? 'lightblue' : 'pink';
    ctx.lineWidth = 4;
    ctx.stroke();
    setTimeout(() => {
        ctx.strokeStyle = line.player === 1 ? 'blue' : 'red';
        ctx.lineWidth = 2;
        ctx.stroke();
    }, 100);
}

function drawBox(box) {
    ctx.fillStyle = box.player === 1 ? 'rgba(0, 0, 255, 0.2)' : 'rgba(255, 0, 0, 0.2)';
    // Box fill animation
    ctx.fillRect(box.x, box.y, dotDistance, dotDistance);
    ctx.fillStyle = box.player === 1 ? 'rgba(0, 0, 255, 0.4)' : 'rgba(255, 0, 0, 0.4)';
    setTimeout(() => {
        ctx.fillRect(box.x, box.y, dotDistance, dotDistance);
    }, 100);
}

function getClickedDot(x, y) {
    let clickedDot = null;
    for (let row = 0; row < gridSize; row++) {
        for (let col = 0; col < gridSize; col++) {
            const dot = dots[row][col];
            const distance = Math.sqrt((x - dot.x) ** 2 + (y - dot.y) ** 2);
            if (distance < dotRadius) {
                clickedDot = dot;
                break;
            }
        }
         if (clickedDot) {
            break;
        }
    }

    if (!clickedDot || !firstDot) {
        return clickedDot;
    }

    const row1 = dots.findIndex(row => row.includes(firstDot));
    const col1 = dots[row1].findIndex(dot => dot === firstDot);
    const row2 = dots.findIndex(row => row.includes(clickedDot));
    const col2 = dots[row2].findIndex(dot => dot === clickedDot);


    if (Math.abs(row1 - row2) + Math.abs(col1 - col2) !== 1) {
        return null;
    }

    return clickedDot;
}

function isLineAlreadyDrawn(dot1, dot2) {
    for (const line of lines) {
        if ((line.from === dot1 && line.to === dot2) || (line.from === dot2 && line.to === dot1)) {
            return true;
        }
    }
    return false;
}

function checkForBoxClosure() {
    let boxesClosed = 0;
    for (let row = 0; row < gridSize - 1; row++) {
        for (let col = 0; col < gridSize - 1; col++) {
            const topLeft = dots[row][col];
            const topRight = dots[row][col + 1];
            const bottomLeft = dots[row + 1][col];
            const bottomRight = dots[row + 1][col + 1];

            const boxLines = [
                [topLeft, topRight],
                [topRight, bottomRight],
                [bottomRight, bottomLeft],
                [bottomLeft, topLeft]
            ];

            const boxAlreadyExists = boxes.some(existingBox => {
                const existingBoxLines = existingBox.lines;
                return boxLines.every(line =>
                    existingBoxLines.some(existingLine =>
                        (existingLine[0] === line[0] && existingLine[1] === line[1]) ||
                        (existingLine[0] === line[1] && existingLine[1] === line[0])
                    )
                );
            });


            if (isLineAlreadyDrawn(topLeft, topRight) &&
                isLineAlreadyDrawn(topRight, bottomRight) &&
                isLineAlreadyDrawn(bottomRight, bottomLeft) &&
                isLineAlreadyDrawn(bottomLeft, topLeft) &&
                !boxAlreadyExists
               ) {
                    boxes.push({ x: topLeft.x, y: topLeft.y, player: currentPlayer, lines: boxLines });
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
            const boxesClosed = checkForBoxClosure();
            scores[currentPlayer] += boxesClosed;
            updateScore();
            if (boxesClosed === 0) {
                currentPlayer = currentPlayer === 1 ? 2 : 1;
            }
            firstDot = null;
            drawBoard();
        }  else {
            firstDot = clickedDot;
        }
    }
});

let firstDot = null;
init();
updateScore();
