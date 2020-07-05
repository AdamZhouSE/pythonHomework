def f(a,b,c,d):
    if a[0] == b[0] or c[0] == d[0]:
        if b[0] == a[0] and c[0] == d[0]:
            return 0
        else:
            return 1
    else:
        k1 = (a[1]-b[1])/(a[0]-b[0])
        b1 = a[1]-k1*a[0]
        k2 = (c[1]-d[1])/(c[0]-d[0])
        b2 = c[1]-k2*c[0]
        if k1==k2:
            return 0
        else:
            if b1 == b2:
                return 0
            else:
                return 1

t = int(input())
for i in range(t):
    points = []
    for index in range(2):
        lst = list(map(int,input().split(' ')))
        points.append([lst[0],lst[1]])
        points.append([lst[2],lst[3]])
    print(f(points[0],points[1],points[2],points[3]))