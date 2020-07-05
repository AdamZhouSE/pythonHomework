from enum import Enum

class state(Enum):
    Pending = 'Pending'
    Draw = 'Draw'
    A = 'A'
    B = 'B'

def play_game(moves):
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = True
    steps = 0
    while steps < len(moves) / 2:
        x = int(moves[steps * 2][-1])
        y = int(moves[steps * 2 + 1][0])
        if player:
            board[x][y] = 1
        else:
            board[x][y] = 2
        player = not player
        steps += 1

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 1:
                return state.A
            elif board[i][0] == 2:
                return state.B
        elif board[1][i] == board[0][i] == board[2][i]:
            if board[0][i] == 1:
                return state.A
            elif board[0][i] == 2:
                return state.B

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == 1:
            return state.A
        elif board[1][1] == 2:
            return state.B
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return state.Pending
        return state.Draw

moves = input().split(',')
print(play_game(moves).value)