def gauss(target):
    try:
        for a in range(n - 1):
            for b in range(a + 1, n):
                theQ = target[b][a] / target[a][a]
                for c in range(a, n):
                    target[b][c] -= theQ * target[a][c]
        result = 1
        for a in range(n - 1):
            result *= target[a][a]
        return int(abs(result))
    except ZeroDivisionError:
        return 0


def cleanMatrix():
    for a in range(n):
        for b in range(n):
            matrix[a][b] = 0


n = int(input())
matrix = []
companies = []
# 记录各个公司负责修的道路
for i in range(n - 1):
    li = input().strip().split(" ")
    count = int(li[0])
    com = []
    for j in range(count):
        com.append([int(li[1 + j * 2]) - 1, int(li[2 + j * 2]) - 1])
    companies.append(com)
start = 2 ** n - 1
# 初始化matrix
for i in range(n):
    ma = []
    for j in range(n):
        ma.append(0)
    matrix.append(ma)

# choose数组用来记录某一公司是否被选择
choose = []
for i in range(n - 1):
    choose.append(True)

result = 0
while start > 0:
    cleanMatrix()
    # 选择施工公司
    for i in range(n - 1):
        if start & (2 ** i) == 0:
            choose[i] = False
        else:
            choose[i] = True
    for i in range(n - 1):
        if choose[i]:
            for road in companies[i]:
                matrix[road[0]][road[0]] += 1
                matrix[road[1]][road[1]] += 1
                matrix[road[0]][road[1]] -= 1
                matrix[road[1]][road[0]] -= 1
    if choose.count(False) % 2 == 0:
        result += gauss(matrix)
    else:
        result -= gauss(matrix)
    start -= 1
print(int(result/2))
