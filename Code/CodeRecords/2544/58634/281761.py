t = int(input())
for i in range(t):
    x1,y1,x2,y2 = map(int,input().split(" "))
    x3,y3,x4,y4 = map(int,input().split(" "))
    if min(x1, x2) <= max(x3, x4) and min(y3, y4) <= max(y1, y2) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4):
        print(1)
    else:
        print(0)
