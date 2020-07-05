moves = eval(input())
chess = [0] + [0, 0, 0] * 3
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
i = -1
for (x, y) in moves:
    i += 1
    if i % 2 == 0: t = 'A'
    else: t = 'B'
    chess[x * 3 + y + 1] = t
    for a, b, c in win:
        if chess[a] == chess[b] and chess[b] == chess[c] and chess[a] != 0:
            print(chess[a])
            exit()
if len(moves) == 9: print('Draw')
else: print('Pending')