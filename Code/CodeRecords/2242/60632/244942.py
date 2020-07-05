inp1 = list(map(int, input().split(',')))
inp2 = list(map(int, input().split(',')))
# rec中包含其中一个矩形的四个顶点的坐标
rec = [[inp1[0], inp1[3]], inp1[:2], [inp1[2], inp1[1]], inp1[2:]]
# area中包含另一个矩形覆盖的横、纵坐标范围
area = [inp2[::2], inp2[1::2]]
judge = False
for i in rec:
    if i[0] in range(area[0][0]+1,area[0][1]) and i[1] in range(area[1][0]+1, area[1][1]):
        judge = True
print(judge)
