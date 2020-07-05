lch = []
rch = []
res_pre_order = []
res_in_order = []
res_post_order = []


def print_pre_order(root):
    if lch[root] == 0 and rch[root] == 0:
        res_pre_order.append(root)
        return
    res_pre_order.append(root)
    if lch[root]!=0:
        print_pre_order(lch[root])
    if rch[root]!=0:
        print_pre_order(rch[root])


def print_in_order(root):
    if lch[root] == 0 and rch[root] == 0:
        res_in_order.append(root)
        return
    if lch[root]!=0:
        print_in_order(lch[root])
    res_in_order.append(root)
    if rch[root]!=0:
        print_in_order(rch[root])


def print_post_order(root):
    if lch[root] == 0 and rch[root] == 0:
        res_post_order.append(root)
        return
    if lch[root]!=0:
        print_post_order(lch[root])
    if rch[root]!=0:
        print_post_order(rch[root])
    res_post_order.append(root)


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
    print_pre_order(root)
    for each in res_pre_order:
        print(each, end=' ')
    print()
    print_in_order(root)
    for each in res_in_order:
        print(each, end=' ')
    print()
    print_post_order(root)
    for each in res_post_order[:-1]:
        print(each, end=' ')
    print(res_post_order[-1])