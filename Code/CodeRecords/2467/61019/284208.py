t = eval(input())
for _ in range(t):
    m, n, k = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    loc1, loc2 = 0, 0
    last = 0
    while k:
        k -= 1
        x = -1e18 if loc1 >= m else a[loc1]
        y = -1e18 if loc2 >= n else b[loc2]
        if x < y:
            loc1 += 1
            last = x
        else:
            loc2 += 1
            last = y
    print(last)
