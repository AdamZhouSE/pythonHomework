def build(l1, r1, l2, r2):
    global last
    global mid
    global lch
    global rch
    if l1 > r1:
        return 0
    root = last[r2]
    p = l1
    while mid[p] != root:
        p += 1
    cnt = p - l1
    lch[root] = build(l1, p-1, l2, l2+cnt-1)
    rch[root] = build(p+1, r1, l2+cnt, r2-1)
    return root


def dfs(v, sum):
    global best
    global bestsum
    global last
    sum += v
    if lch[v]==0 and rch[v]==0:
        if sum < bestsum or (sum==bestsum and v<best):
            best = v
            bestsum = sum
    if lch[v] != 0:
        dfs(lch[v], sum)
    if rch[v] != 0:
        dfs(rch[v], sum)

if __name__ == '__main__':
    mid = list(int(n) for n in input().split(' '))
    last = list(int(n) for n in input().split(' '))
    n = len(mid)
    lch = [0]*1000
    rch = [0]*1000
    build(0, n-1, 0, n-1)
    bestsum = 0x3f3f3f3f
    best = 0
    dfs(last[n-1], 0)
    print(best)