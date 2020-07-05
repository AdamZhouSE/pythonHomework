def ec(n,connections):
    if len(connections) < n - 1:
        print(-1)
        return
    fa = [x for x in range(n)]
    def findset(x):
        if x != fa[x]:
            fa[x] = findset(fa[x])
        return fa[x]
    part = n
    for c0, c1 in connections:
        p, q = findset(c0), findset(c1)
        if p != q:
            part -= 1
            fa[p] = q
    print(part - 1)
if __name__ == '__main__':
    ec(int(input()),eval(input()))
