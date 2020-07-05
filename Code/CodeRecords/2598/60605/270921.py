INF = 9999999999999

def update(tree: [int], l: int, r: int, pos: int, tar: int, val: int):
    if l == r:
        tree[pos] = val
        return
    mid = (l + r) // 2
    if tar <= mid:
        update(tree, l, mid, 2*pos+1, tar, val)
    else:
        update(tree, mid+1, r, 2*pos+2, tar, val)
    tree[pos] = max(tree[2*pos+1], tree[2*pos+2])

def query(tree: [int], pos: int, l: int, r: int, currl: int, currR: int) -> int:
    if currl > r or currR < l: return -INF
    if currl <= l and currR >= r:
        return tree[pos]
    mid = (l + r) // 2
    return max(query(tree, 2*pos+1, l, mid, currl, currR), query(tree, 2*pos+2, mid+1, r, currl, currR))


if __name__ == '__main__':
    x = input().strip().split()
    m = int(x[0])
    d = int(x[1])
    ops = []
    for i in range(m):
        x = input().strip().split()
        ops.append([x[0], int(x[1])])
    tree = [0 for i in range(4*m)]
    lastPos = 0
    t = 0
    for op in ops:
        if op[0] == "A":
            tt = (t + op[1]) % d
            update(tree, 1, m, 0, lastPos+1, tt)
            lastPos += 1
        else:
            tt = op[1]
            t = query(tree, 0,1, m, lastPos-tt+1, lastPos)
            print(t)