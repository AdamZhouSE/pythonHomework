tmp = input()
tmp = [int(x) for x in tmp.split(" ")]
n = tmp[0]
x0 = tmp[1]
y0 = tmp[2]
res = []
for i in range(n):
    tmp = input()
    tmp = [int(x) for x in tmp.split(" ")]
    x1 = tmp[0]
    y1 = tmp[1]
    exist = False
    for x in res:
        x2 = x[0]
        y2 = x[0]
        if (y2 - y0) * (x1 - x0) == (y1 - y0) * (x2 - x0):
            exist = True
            break
    if not exist:
        res.append([x1, y1])
print(len(res))
