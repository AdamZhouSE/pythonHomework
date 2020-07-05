[H, W, K] = list(map(int, input().split(" ")))
H_times = H
W_times = W
net = []
for i in range(0, H):
    net.append(list(input()))

# 输入完成 开始分形

net_origin = net.copy()
for i in range(0, K-1):
    H = H * H_times
    W = W * W_times
    temp = [['.' for _ in range(0, W)] for _ in range(0, H)]
    for j in range(0, len(net)):
        for k in range(0, len(net[0])):
            if net[j][k] == '#':
                for l in range(H_times * j, H_times * (j+1)):
                    for m in range(W_times * k, W_times * (k+1)):
                        temp[l][m] = net_origin[l % H_times][m % W_times]
    net = temp

# 分形完成


def dfs(matrix, i, j):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
        try:
            if matrix[i][j] == matrix[i-1][j] == matrix[i+1][j] == matrix[i][j-1] == matrix[i][j+1] == '.':
                return
        finally:
            if matrix[i][j] == '#':
                matrix[i][j] = '.'
                dfs(matrix, i-1, j)
                dfs(matrix, i+1, j)
                dfs(matrix, i, j+1)
                dfs(matrix, i, j-1)


count = 0
for i in range(0, len(net)):
    for j in range(0, len(net[0])):
        if net[i][j] == '#':
            count += 1
            dfs(net, i, j)
print(count)



