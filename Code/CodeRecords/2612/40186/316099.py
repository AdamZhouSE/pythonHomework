t = int(input())
points = []
for i in range(t):
    n = int(input())
    for j in range(n):
        temp = input().split(' ')
        points.append([int(temp[0]),int(temp[1])])
print(points)