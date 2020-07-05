from collections import namedtuple
def test():
    point = namedtuple('point',['x','y'])
    points = []
    t = int(input())
    for i in range(t):
        n = int(input())
        for j in range(n):
            lst = list(map(int,input().split(' ')))
            points.append(point(lst[0],lst[1]))
    print(points)

print(0)
if input():
    test()
   