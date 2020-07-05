t = int(input())
for x in range(t):
    x1, y1, x2, y2 = [int(i) for i in input().split()]
    x3, y3, x4, y4 = [int(i) for i in input().split()]
    if not (min(x1,x2) <= max(x3,x4) and min(y3,y4) <= max(y1,y2) and min(x3,x4) <= max(x1,x2) and min(y1,y2) <= max(y3,y4)):
        print(0)
        break
    else:
        fc = (y3-y1) * (x2-x1) - (x3-x1) *(y2-y1)
        fd = (y4-y1) * (x2-x1) - (x4-x1) *(y2-y1)
        if(fc * fd > 0):
            print(0)
            break
    print(1)
