def check_win(color):
    board = [0] * 9
    for c in color:
        board[c] = 1
    cond = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
    return sum([board[a] * board[b] * board[c] for a, b, c in cond]) > 0


xs = eval(input())
loc = [3 * r[0] + r[1] for r in xs]
side, A, B = 0, [], []
for i in loc:
    if side % 2 == 0:
        A.append(i)
        if check_win(A):
            print('A')
            exit(0)
    else:
        B.append(i)
        if check_win(B):
            print('B')
            exit(0)
    side += 1
if len(loc) == 9:
    print('Draw')
    exit(0)
else:
    print('Pending')
    exit(0)
