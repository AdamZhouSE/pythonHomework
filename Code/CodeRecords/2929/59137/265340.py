def s32():
    s = input().split()
    n = int(s[0])
    m = int(s[1])

    size = []
    dif = []
    for i in range(n):
        s = input().split()
        size.append(int(s[0]))
        dif.append(int(s[0]) - int(s[1]))

    count = 0
    now = sum(size)
    dif = list(sorted(dif, reverse=True))

    for i in range(n):
        if now <= m:
            break
        now = now - dif[i]
        count = count + 1

    if count == n:
        if now > m:
            count = -1
    print(count)


s32()