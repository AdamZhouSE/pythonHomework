def f(a,b,c,d):
    if b[0] == a[0] and c[0] == d[0]:
        return 0
    else:
        if (a[1]-b[1])/(a[0]-b[0]) == (c[1]-d[1])/(c[0]-d[0]):
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