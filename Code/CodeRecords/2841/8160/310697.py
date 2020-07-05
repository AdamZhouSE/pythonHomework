tmp = input()
n, m = [int(i) for i in tmp.split(" ")]
arr = input()
arr = [int(i) for i in arr.split(" ")]
maxN = 300000
ff = [0 for i in range(maxN << 2)]
sum = [0 for i in range(maxN << 2)]
arr.insert(0, 0)



def pb(rt):
    if ff[rt] % 2 == 0:
        sum[rt] = sum[rt << 1 | 1] | sum[rt << 1]
    else:
        sum[rt] = sum[rt << 1 | 1] ^ sum[rt << 1]


def build(l, r, rt):
    sum[rt] = 0
    ff[rt << 1] = 0
    ff[rt << 1 | 1] = 0
    if l == r:
        sum[rt] = arr[l]
        ff[rt] = -1
        return
    mid = (l + r) >> 1
    build(l, mid, rt << 1)
    build(mid + 1, r, rt << 1 | 1)
    ff[rt] = ff[rt << 1] + 1
    pb(rt)


def update(l, r, p, d, rt):
    if l == r:
        sum[rt] = d
        return
    mid = (l + r) >> 1
    if p <= mid:
        update(l, mid, p, d, rt << 1)
    else:
        update(mid + 1, r, p, d, rt << 1 | 1)
    pb(rt)


num = 1 << n
ff[1] = 1
build(1, num, 1)
for i in range(m):
    tmp = input()
    u, v = [int(k) for k in tmp.split(" ")]
    update(1, num, u, v, 1)
    print(sum[1])
