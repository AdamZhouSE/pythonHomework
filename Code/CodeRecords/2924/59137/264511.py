def s28():
    s = input().split()
    n = int(s[0])
    r = int(s[1])
    avg = int(s[2])

    a = []
    b = []
    for i in range(n):
        s = input().split()
        a.append(int(s[0]))
        b.append(int(s[1]))

    target = avg * n
    now = sum(a)
    count = 0

    while now < target:
        m = min(b)
        i = b.index(m)
        if target - now >= r - a[i]:
            num = r - a[i]
        else:
            num = target - now

        now = now + num
        count = count + m * num

        b.pop(i)
        a.pop(i)

    print(count)


s28()