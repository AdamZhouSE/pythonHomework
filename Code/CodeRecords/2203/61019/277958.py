def mys(xs, a, b):
    mys_len = 0
    try:
        while xs[a] == xs[b]:
            mys_len += 1
            a += 1
            b += 1
    except IndexError:
        pass
    res = 0
    for i in range(b - a, mys_len):
        res += i + 1
    return res


s = input()
n = len(s)
for i in range(n):
    xs = s[:i + 1]
    res = sum([mys(xs, a, b) for a in range(i) for b in range(i) if a < b])
    print(res)
