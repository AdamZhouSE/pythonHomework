n = int(input())
board = [[] * n] * n
for i in range(n):
    board[i] = list(input())
bl = False
for i in range(n):
    bl = True
    for j in range(n):
        up = i - 1
        down = i + 1
        left = j - 1
        right = j + 1
        num = 0
        if up >= 0:
            if board[up][j] == "o":
                num += 1
        if down < n:
            if board[down][j] == "o":
                num += 1
        if left >= 0:
            if board[i][left] == "o":
                num += 1
        if right < n:
            if board[i][right] == "o":
                num += 1
        if num % 2 != 0:
            bl = False
            break
    if bl == False:
        break
print("YES" if bl else "NO")

