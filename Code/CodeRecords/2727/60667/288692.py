import math
t = int(input())
for i in range(t):
    n = int(input())
    mouses = list(map(int, input().split()))
    holes = list(map(int, input().split()))
    mouses.sort()
    holes.sort()
    temp = []
    for j in range(len(mouses)):
        temp.append(math.fabs(mouses[j]-holes[j]))
    print(int(max(temp)))    