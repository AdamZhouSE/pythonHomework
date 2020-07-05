m, n = list(map(int, input().split(' ')))
chess = [list(input()) for _ in range(m)]
left_up = right_down = (-1, -1)
for i in range(m):
    for j in range(n):
        if chess[i][j] == 'B':
            if left_up == (-1, -1):
                left_up = (i, j)
            right_down = (i, j)
print((left_up[0] + right_down[0]) // 2 + 1, (left_up[1] + right_down[1]) // 2 + 1)