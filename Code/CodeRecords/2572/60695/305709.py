lto = input().split(" ")
l, t, o = int(lto[0]), int(lto[1]), int(lto[2])
op = []
for i in range(o):
    x = input().split(" ")
    op.append(x)
board = [1] * l
for i in range(o):
    if op[i][0] == 'C':
        l, r, c = int(op[i][1]), int(op[i][2]), int(op[i][3])
        for j in range(l - 1, r):
            board[j] = c
    else:
        l, r = int(op[i][1]), int(op[i][2])
        s = ""
        for j in range(l - 1, r):
            s = s + str(board[j])
        from collections import Counter
        c = Counter(s)
        print(len(c))

