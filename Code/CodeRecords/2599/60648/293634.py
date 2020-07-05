INF = 99999999


def build(tree: [int], ori: [int], l: int, r: int, pos: int):
    if l == r:
        tree[pos] = ori[l-1]
        return
    mid = (l + r) // 2
    build(tree, ori, l, mid, 2*pos+1)
    build(tree, ori, mid+1, r, 2*pos+2)
    tree[pos] = min(tree[2*pos+1], tree[2*pos+2])

def queryMin(tree: [int], l: int, r: int, needl: int, needr: int, pos: int) -> int:
    if needr < l or needl > r:
        return INF
    if needl <= l and needr >= r:
        return tree[pos]
    mid = (l+r) // 2
    return min(queryMin(tree, l, mid, needl, needr, 2*pos+1), queryMin(tree, mid+1, r, needl, needr, 2*pos+2))

def insertCow(tree: [int], l: int, r: int, needl: int, needr: int, pos: int):
    if needl <= l <= needr and l == r:
        tree[pos] -= 1
        return
    if needr < l or needl > r:
        return
    mid = (l+r)//2
    insertCow(tree, l, mid, needl, needr, 2*pos+1)
    insertCow(tree, mid+1, r, needl, needr, 2*pos+2)
    tree[pos] = min(tree[2*pos+1], tree[2*pos+2])
    return



if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0]) # fence
    m = int(x[1]) # cowreqs
    fences = []
    cowreq = []
    for i in range(n):
        fences.append(int(input()))
    for i in range(m):
        x = input().strip().split()
        # Ai, Bi
        cowreq.append([int(x[0]), int(x[1])])
    # 排序
    cowreq = sorted(cowreq, key=lambda vi: (vi[1], (vi[1] - vi[0])))
    tree = [0 for i in range(4*n+1)]
    build(tree, fences, 1, n, 0)
    cnt = 0
    for i in cowreq:
        minVal = queryMin(tree, 1, n, i[0], i[1], 0)
        if minVal > 0:
            insertCow(tree, 1, n, i[0], i[1], 0)
            cnt += 1
    print(cnt)
