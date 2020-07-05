t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().split(' ')]
    h = [max(a)] * n
    xx = 20

    unstable = set(range(n))


    def be_stable(k):
        lh = max(h[k - 1] if k > 0 else 0, a[k])
        rh = max(h[k + 1] if k < n - 1 else 0, a[k])
        if h[k] > lh:
            h[k] = lh
            unstable.add(k + 1)
            if k > 0:
                unstable.add(k - 1)
        if h[k] > rh:
            h[k] = rh
            unstable.add(k - 1)
            if k < n - 1:
                unstable.add(k + 1)


    while unstable:
        index = unstable.pop()
        be_stable(index)
   # print(h)
    print(sum(h) - sum(a))
