<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe</title>
    <style>
    body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color:#c5c6c7;
}

.board {
    display: grid;
    grid-template-columns: repeat(3, 100px);
    grid-template-rows: repeat(3, 100px);
    gap: 5px;
}

.cell {
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #000;
    font-size: 2em;
    background-color:#b3b4bd ;
    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.cell:hover {
    background-color: #adbbda;
    cursor: pointer;
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

.cell.X {
    color: blue;
}

.cell.O {
    color: red;
}

.hidden {
    display: none;
}

h1, p {
    text-align: center;
}

</style>
    
</head>
<body>
    <h1>Tic-Tac-Toe</h1>
    <div class="board" id="board"></div>
    <p id="message"></p>
    <script>
        const EMPTY = "-";
        const PLAYER_X = "X";
        const PLAYER_O = "O";
        const SIZE = 9;

        let board = Array(SIZE).fill(EMPTY);
        let currentPlayer = PLAYER_X;
        let gameRunning = true;
        let winner = null;

        const boardElement = document.getElementById('board');
        const messageElement = document.getElementById('message');

        function createBoard() {
            boardElement.innerHTML = '';
            board.forEach((cell, index) => {
                const cellElement = document.createElement('div');
                cellElement.classList.add('cell');
                cellElement.textContent = cell;
                cellElement.addEventListener('click', () => playerMove(index));
                boardElement.appendChild(cellElement);
            });
        }

        function printBoard() {
            createBoard();
        }

        function playerMove(index) {
            if (board[index] === EMPTY && gameRunning) {
                board[index] = currentPlayer;
                printBoard();
                if (checkWinner()) {
                    messageElement.textContent = `The winner is ${winner}!`;
                    gameRunning = false;
                } else if (checkTie()) {
                    messageElement.textContent = "It's a tie!";
                    gameRunning = false;
                } else {
                    switchPlayer();
                    if (currentPlayer === PLAYER_O) {
                        setTimeout(computerMove, 500);
                    }
                }
            }
        }

        function checkWinner() {
            const winConditions = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]
            ];
            for (const condition of winConditions) {
                const [a, b, c] = condition;
                if (board[a] === board[b] && board[b] === board[c] && board[a] !== EMPTY) {
                    winner = board[a];
                    return true;
                }
            }
            return false;
        }

        function checkTie() {
            return board.every(cell => cell !== EMPTY);
        }

        function switchPlayer() {
            currentPlayer = currentPlayer === PLAYER_X ? PLAYER_O : PLAYER_X;
        }

        function computerMove() {
            if (!gameRunning) return;
            let position;
            do {
                position = Math.floor(Math.random() * SIZE);
            } while (board[position] !== EMPTY);
            board[position] = PLAYER_O;
            printBoard();
            if (checkWinner()) {
                messageElement.textContent = `The winner is ${winner}!`;
                gameRunning = false;
            } else if (checkTie()) {
                messageElement.textContent = "It's a tie!";
                gameRunning = false;
            } else {
                switchPlayer();
            }
        }

        printBoard();
    </script>
</body>
</html>
