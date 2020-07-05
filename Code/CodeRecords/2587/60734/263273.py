n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split(','))))

steps = 0
for i in range(1,len(points)):
    x = abs(points[i][0]-points[i-1][0])
    y = abs(points[i][1]-points[i-1][1])
    steps+=max(x,y)
print(steps)