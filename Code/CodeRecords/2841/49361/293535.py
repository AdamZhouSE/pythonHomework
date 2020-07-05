tmp = input()
n, m = [int(i) for i in tmp.split(" ")]
arr = input()
arr = [int(i) for i in arr.split(" ")]
maxN = 300000 + 7

tr = [0 for i in range(maxN)]


class Tree:
    def __init__(self, l, r, sum=0):
        self.l = l
        self.r = r
        self.sum = sum

    def mid(self):
        return (self.l + self.r) >> 1


def build(p, l, r):
    tr[p] = Tree(l, r)
    if l == r:
        return
    mid = tr[p].mid()
    build(p << 1, l, mid)
    build(p << 1 | 1, mid + 1, r)


def update(p, pos, x, cur):
    if tr[p].l == tr[p].r:
        tr[p].sum = x
        return
    mid = tr[p].mid()
    if pos <= mid:
        update(p << 1, pos, x, cur - 1)
    else:
        update(p << 1 | 1, pos, x, cur - 1)
    if cur % 2 == 0:
        tr[p].sum = tr[p << 1].sum | tr[p << 1 | 1].sum
    else:
        tr[p].sum = tr[p << 1].sum ^ tr[p << 1 | 1].sum


num = 1 << n
build(1, 1, num)
for i in range(num):
    update(1, i, arr[i], n + 1)
for m in range(m):
    u, v = [int(i) for i in tmp.split(" ")]
    update(1, u, v, n + 1)
    print(tr[1].sum)
