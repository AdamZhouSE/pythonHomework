t = int(input())
for i in range(t):
    x1,y1,x2,y2 = map(int,input().split(" "))
    x3,y3,x4,y4 = map(int,input().split(" "))
    if min(x1, x2) <= max(x3, x4) and min(y3, y4) <= max(y1, y2) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4):
        u = (x3-x1)*(y2-y1)-(x2-x1)*(y3-y1)
        v = (x4-x1)*(y2-y1)-(x2-x1)*(y4-y1)
        w = (x1-x3)*(y4-y3)-(x4-x3)*(y1-y3)
        z = (x2-x3)*(y4-y3)-(x4-x3)*(y2-y3)
        if u*v<=0 and w*z <=0:
            print(1)
        else:
            print(0)
    else:
        print(0)
