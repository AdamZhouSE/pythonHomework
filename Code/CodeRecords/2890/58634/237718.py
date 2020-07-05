a = [int(i) for i in input().split(" ")]
n = a[0]
x = a[1]
y = a[2]
different_k = []
not_have_k = False #与原点的连线垂直于x轴，没有斜率的
for i in range(n):
    b = [int(i) for i in input().split(" ")]
    x1 = b[0] - x#移动坐标轴，把意大利炮放在原点
    y1 = b[1] - y
    if x1 == 0:
        not_have_k = True
    else:
        if different_k.count(y1/x1) == 0:
            different_k.append(y1/x1)
if not_have_k:
    print(len(different_k)+1)
else:
    print(len(different_k))