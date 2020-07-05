n, c = map(int, input().split())
a = list(map(int, input().split()))
if c == 0:
    print(0)
else:
    i = 1
    while n > 1:
        n = n - 1
        if a[n] - a[n-1] <= c:
            i += 1
        else:
            break
    print(i)
