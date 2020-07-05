
t = int(input())
for i in range(0, t):
    nn = int(input())
    a = input().split(' ')
    a = list(map(int, a))
    a.sort()
    n = len(a)
    sum1 = 0
    sum2 = 0
    for i in range(0, n):
        sum1 += a[i]
    d = 0
    min_d = abs(sum1 - sum2)
    while True:
        k = -1
        for i in range(0, n):
            d = abs(sum1 - sum2 - a[i] - a[i])
            if d < min_d:
                min_d = d
                k = i
        if k != -1:
            sum1 -= a[k]
            sum2 += a[k]
            a[k] = 0
        if k == -1:
            break
    print(min_d)