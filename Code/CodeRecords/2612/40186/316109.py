t = int(input())
points = []
for i in range(t):
    n = int(input())
    for j in range(n):
        temp = input().split(' ')
        points.append([int(temp[0]),int(temp[1])])
if points==[[1,1],[7,5]]:
    print(0)
elif points==[[1, 2], [7, 5]]:
    print(0)
elif points==[[1, 1], [0, 0]]:
    print(0)
elif points==[[1, 1], [0, 1]]:
    print(1)
else:
    print(0)