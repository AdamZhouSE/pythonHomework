a = list(map(int, input().split(",")))
x1 = a[0:2]
x2 = a[2:4]
y1 = a[4:6]
y2 = a[6:8]
if x2[1] < y2[1]:
    temp1 = x1
    temp2 = x2
    x1 = y1
    x2 = y2
    y1 = temp1
    y2 = temp2
s = (x2[0] - x1[0]) * (x2[1] - x1[1]) + (y2[0] - y1[0]) * (y2[1] - y1[1])
if x2[0] <= y1[0] or x1[0] >= y2[0] or x1[1] >= y2[1]:
    s = s
elif x1[0] < y1[0]:
    if y2[0] > x2[0]:
        s -= (x2[0] - y1[0]) * (y2[1] - x1[1])
    else:
        s -= (y2[1] - x1[1]) * (y2[0] - y1[0])
elif x1[0] >= y1[0]:
    if y2[0] < x2[0]:
        s -= (y2[0] - x1[0]) * (y2[1] - x1[1])
    else:
        s -= (x2[0] - x1[0]) * (y2[1] - x1[1])
print(s)
