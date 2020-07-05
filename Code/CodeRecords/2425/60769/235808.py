num = int(input())
for i in range(num):
    n, k = list(map(int,input().split(" ")))
    l = list(map(int,input().split(" ")))
    res = 0
    min = 99999999
    for j in range(n):
        if abs(l[j] - k) <= min:
            min = abs(l[j] - k)
            res = l[j]
    print(res)
