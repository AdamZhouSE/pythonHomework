from itertools import combinations
N=int(input())
points=[]
for i in range(N):
    x,y=map(int,input().split(","))
    points.append((x,y))
print(max(abs((x0-x2)*(y1-y2)-(x1-x2)*(y0-y2)) for (x0,y0),(x1,y1),(x2,y2) in combinations(points,3))/2)