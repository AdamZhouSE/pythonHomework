for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    lmax = a[0]
    rmax = max(a[1:])
    count = 0
    for i in range(n):
        if a[i] > lmax:
            lmax = a[i]
        if (a[i] == rmax and i < n - 1):
            rmax = max(a[i + 1:])
        h = min(lmax, rmax)
        count += max(h - a[i], 0)
    print(count)