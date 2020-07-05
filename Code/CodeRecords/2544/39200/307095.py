t = int(input())
for x in range(t):
    x1, y1, x2, y2 = [int(i) for i in input().split()]
    x3, y3, x4, y4 = [int(i) for i in input().split()]
    flag = 1
    if not (min(x1,x2) <= max(x3,x4) and min(y3,y4) <= max(y1,y2) and min(x3,x4) <= max(x1,x2) and min(y1,y2) <= max(y3,y4)):
        flag = 0
    else:
        acab = (y3-y1) * (x2-x1) - (x3-x1) *(y2-y1)
        adab = (y4-y1) * (x2-x1) - (x4-x1) *(y2-y1)
        if(acab * adab > 0):
            flag = 0
    print(flag)
