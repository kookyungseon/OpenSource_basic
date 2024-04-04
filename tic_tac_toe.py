import random

def draw_board(board):
    for r in range(3):
        print("  " + board[r][0] + "| " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Winner in a row
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Winner in a column
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Winner in the main diagonal
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Winner in the anti-diagonal
    return None

def is_board_full(board):
    # Check if the board is full (no empty cells)
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

def player_move(board):
    while True:
        try:
            row, col = map(int, input("위치를 선택하세요 (행, 열): ").split(','))
            if board[row][col] == ' ':
                return row, col
            else:
                print("이미 선택된 위치입니다. 다른 위치를 선택하세요.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 행과 열을 0부터 2까지의 숫자로 입력하세요.")

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        draw_board(board)

        if player == 'X':
            x, y = player_move(board)
        else:
            x, y = computer_move(board)
            print(f"컴퓨터가 {x}, {y}에 놓았습니다.")

        board[x][y] = player

        winner = check_winner(board)
        if winner:
            draw_board(board)
            print(f"{winner} 플레이어가 이겼습니다!")
            break
        elif is_board_full(board):
            draw_board(board)
            print("무승부입니다!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
