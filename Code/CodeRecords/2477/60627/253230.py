# 11
n = int(input())
for i in range(n):
    x1,y1,x2,y2 = input().split()
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    x3,y3,x4,y4 = input().split()
    x3,y3,x4,y4 = int(x3),int(y3),int(x4),int(y4)
    
    if (x1<x3<x2 and y2<y3<y1) or (x1<x4<x2 and y2<y4<y1):
        print(1)
    else:
        print(0)