t = int(input())
result = []
data = []
for i in range(2*t):
    data.append(list(map(int, input().split(' '))))
data[0] = [data[0][0], data[0][3], data[0][2], data[0][1]]
data[1] = [data[1][0], data[1][3], data[1][2], data[1][1]]
for i in range(0, len(data), 2):
    inp1 = data[i]
    inp2 = data[i+1]
    # rec中包含其中一个矩形的四个顶点的坐标
    rec = [[inp1[0], inp1[3]], inp1[:2], [inp1[2], inp1[1]], inp1[2:]]
    # area中包含另一个矩形覆盖的横、纵坐标范围
    area = [inp2[::2], inp2[1::2]]
    judge = 0
    for i in rec:
        if i[0] in range(area[0][0] + 1, area[0][1]) and i[1] in range(area[1][0] + 1, area[1][1]):
            judge = 1
    result.append(judge)
for i in result:
    print(i)
