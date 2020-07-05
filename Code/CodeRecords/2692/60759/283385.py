weights = eval(input())
days = int(input())
board = max(weights)
while True:
    this_board = 0
    idx = -1
    for day in range(0, days):
        while this_board < board and idx < len(weights) - 1:
            idx += 1
            this_board += weights[idx]
        if this_board > board:
            idx -= 1
        this_board = 0
    if idx == len(weights) - 1:
        break
    board += 1
print(board)
