Max = 4000010
f = [0 for i in range(Max)]


def find(x: int):
    if x == f[x]:
        return x
    else:
        f[x] = find(f[x])
        return f[x]


if __name__ == '__main__':
    T = eval(input())
    res = []
    for t in range(T):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        tag = int(m < n + 2)
        for i in range(1, n << 1 + 1):
            f[i] = i
        for i in range(1, m + 1):
            xy = input().split()
            x = int(xy[0])
            y = int(xy[1])
            f[find(x)] = find(y + n)
            f[find(y)] = find(x + n)
        for i in range(n + 1):
            if tag:
                tag &= (find(i) != find(i + n))
        if tag:
            res.append('YES')
        else:
            res.append('NO')
    for r in res:
        print(r)