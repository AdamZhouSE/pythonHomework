
from collections import Counter

n=int(input())
points=[]
for i in range(0,n):
    temp1=list(map(int,input().split(',')))
    points.append(temp1)


def K(i, j):
        return float('Inf') if i[1] - j[1] == 0 else (i[0] - j[0]) / (i[1] - j[1])


if len(points) <= 2:
    print(len(points))
else:
    maxans = 0
    for i in points:
        same = sum(1 for j in points if j == i)
        hashmap = Counter([K(i, j) for j in points if j != i])
        tempmax = hashmap.most_common(1)[0][1] if hashmap else 0
        maxans = max(same + tempmax, maxans)

    print(maxans)