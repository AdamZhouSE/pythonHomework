def constructor(matrix: list) -> list:  # 根据所给矩阵构造二部图，返回二部图的邻接矩阵
    link = {}
    x_num, y_num = 0, 0  # xi为‘1’的编号，yi为‘3’的编号
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '3':
                key = 'y' + str(y_num)
                matrix[r][c] = key
                y_num += 1
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '1':
                key = 'x' + str(x_num)
                link[key] = []
                x_num += 1
                if r != 0:
                    if matrix[r - 1][c][0] == 'y':  # 上
                        link[key].append(matrix[r - 1][c])
                if r != len(matrix) - 1:
                    if matrix[r + 1][c][0] == 'y':  # 下
                        link[key].append(matrix[r + 1][c])
                if c != 0:
                    if matrix[r][c - 1][0] == 'y':  # 左
                        link[key].append(matrix[r][c - 1])
                if c != len(matrix[0]) - 1:
                    if matrix[r][c + 1][0] == 'y':  # 右
                        link[key].append(matrix[r][c + 1])
                link[key] = sorted(link[key])
    adjacent = []
    for i in range(x_num):
        adjacent.append([0] * y_num)
    for i in range(x_num):
        for j in link['x' + str(i)]:
            adjacent[i][int(j[1:])] = 1
    return adjacent


def find(x):
    for index in range(y):
        if adj[x][index] == 1 and used[index] == 0:  # 如果可匹配，且y还未被尝试匹配过
            used[index] = 1
            if connect[index] == -1 or find(connect[index]) != 0:  # 如果y还未成功匹配，或者x还能匹配到其他y
                connect[index] = x
                return 1
    return 0


n, m = map(int, input().split(' '))
data = []
for i in range(n):
    data.append(list(input()))
adj = constructor(data)
count = 0
if len(adj) != 0 and len(adj[0]) != 0:
    x, y = len(adj), len(adj[0])  # x,y分别为1和3的个数
    connect = [-1 for i in range(y)]
    for i in range(x):
        used = [0 for j in range(y)]
        if find(i):
            count += 1
num_of_2 = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '2':
            num_of_2 += 1
print(count + num_of_2)
