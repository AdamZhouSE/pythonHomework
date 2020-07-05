def makeConnected(n, con) :
    n = int(n)
    if len(con) < n - 1:
        return -1

    p, res = list(range(n)), n

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    for i, j in con:
        px, py = find(i), find(j)
        if px != py:
            p[px] = py
            res -= 1

    return res - 1

n = input()
con = eval(input())
print(makeConnected(n, con))