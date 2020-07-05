from collections import namedtuple
point = namedtuple('point',['x','y'])
points = []
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        lst = list(map(int,input().split(' ')))
        points.append(point(lst[0],lst[1]))

    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if points[i].x == points[j].x or points[i].y == points[j].y:
                    count+=1
    print(count)