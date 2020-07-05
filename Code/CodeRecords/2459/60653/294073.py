def update(pos, k):
    if left[k] == right[k]:
        flg[k] = 1
        return
    mid = (left[k] + right[k]) >> 1
    if pos <= mid:
        update(pos, k<<1)
    else:
        update(pos, k<<1|1)
    flg[k] = flg[k << 1] and flg[k << 1 | 1]


def query(x, k):
    if flg[k] == 1:
        return 0
    if left[k] == right[k]:
        return left[k]
    mid = (left[k]+right[k])>>1
    if x <= mid and flg[k<<1] == 0:
        return query(x, k<<1)
    return query(x, k<<1|1)


def build(l, r, k):
    left[k] = l
    right[k] = r
    if l==r:
        return
    mid = (l+r) >> 1
    build(l, mid, k<<1)
    build(mid+1, r, k<<1|1)
    flg[k] = flg[k<<1] and flg[k<<1|1]

if __name__ == '__main__':
    left = [0]*1000
    right = [0]*1000
    flg = [0]*1000
    id = []
    val = []
    ans = [0]*1000
    n, k = map(int, input().split(' '))
    build(1, n, 1)
    s = list(int(o) for o in input().split(' '))
    for i in range(0, n):
        id.append(i+1)
        val.append(s[i])
    p = sorted(zip(id, val), key=lambda x: x[1])
    p.reverse()
    sum = 0
    for i in range(0, n):
        pos = query(max(1, p[i][0]-k), 1)
        ans[p[i][0]] = pos+k
        update(pos, 1)
        sum += (ans[p[i][0]] - p[i][0])*p[i][1]
    print(sum)
    for i in range(1, n+1):
        print(ans[i], end=' ')