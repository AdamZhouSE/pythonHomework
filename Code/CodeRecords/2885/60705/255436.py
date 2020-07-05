n = int(input())
for i in range(0, n):
    length = int(input())
    d = {1: 0, 2: 0, 3: 0}
    res = 0
    l = list(map(int, input().split(" ")))
    for i in range(length):
        if l[i] in [1, 2, 3]:
            d[l[i]] += 1
    if d[2] >= d[1]:
        res = d[3] + d[1]
    else:
        res = d[3] + d[2] + (d[1] - d[2]) // 3
    print(res)
