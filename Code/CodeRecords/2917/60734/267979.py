n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split(' '))))
count = 0
for i in range(n):
    for j in range(n):
        if points[i][0] == points[j][0]\
        or points[i][1] == points[j][1]:
            count+=1
print(count)