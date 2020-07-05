import math


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().split())
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dstr = ['N', 'E', 'S', 'W']
    oc = [0, 0]
    od = 0
    for i in range(0, len(arr), 2):
        d, x = arr[i], int(arr[i+1])
        if d == 'D': od += 2
        elif d == 'L': od -= 1
        elif d == 'R': od += 1
        od %= 4
        oc[0] += dir[od][0] * x
        oc[1] += dir[od][1] * x
    print(math.floor(math.sqrt(oc[0]**2 + oc[1]**2)), dstr[od])