lch = []
rch = []
res = []


def in_order(root):
    if lch[root] == 0 and rch[root] == 0:
        res.append(root)
        return
    if lch[root]!=0:
        in_order(lch[root])
    res.append(root)
    if rch[root]!=0:
        in_order(rch[root])


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    root = arr[1]
    lch = [0 for i in range(500)]
    rch = [0 for i in range(500)]
    for i in range(n):
        arr = [int(j) for j in input().split()]
        lch[arr[0]] = arr[1]
        rch[arr[0]] = arr[2]
    in_order(root)
    res.append(0)
    print(res[res.index(int(input())) + 1])