example = int(input())
for i in range(0, example):
    n = int(input())
    length = [int(x) for x in input().split()]
    temp = dict()
    for x in range(1, n + 1):
        temp[x] = 0
    for j in range(0, n):
        for k in range(1, n + 1):
            if length[j] >= k:
                temp[k] += 1
    for j in range(n, 0, -1):
        if temp[j] >= j:
            print(j)
            break

