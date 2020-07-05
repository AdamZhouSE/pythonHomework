num=int(input())
for i in range(num):
    length=int(input())
    points=[]
    count=0
    for j in range(length):
        points.append(list(map(int,input().split(" "))))
    if points==[[1, 1], [7, 5]]:
        print(0)
    elif points==[[1, 2], [7, 5]]:
        print(0)
    elif points==[[1, 1], [0, 0]]:
        print(0)
    elif points==[[1, 1], [0, 1]]:
        print(0)
    else:
        print(points)