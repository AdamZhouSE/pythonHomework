def query(i, L, R):
    global ql
    global qr
    global ans

    if ql <= L and qr >= R:
        ans = find(i, L, R)
        return
    mid = L+R>>1
    if ql <= mid:
        query(i<<1, L, mid)
        if ans != 99999:
            return
    if qr > mid:
        query(i<<1|1, mid+1, R)




def find(i, L, R):
    global minv
    global k
    if minv[i] > k:
        return 99999
    elif L == R:
        return L
    mid = L+R>>1
    if minv[i<<1] <= k:
        return find(i<<1, L, mid)
    else:
        return find(i<<1|1, mid+1, R)



def update(i, L, R):
    global minv
    global k
    global x
    if L == R:
        minv[i] = k
        return
    mid = L+R>>1
    if x <= mid:
        update(i<<1, L, mid)
    else:
        update(i<<1|1, mid+1, R)
    minv[i] = min(minv[i<<1], minv[i<<1|1])


if __name__ == '__main__':
    n, q = map(int, input().split(' '))
    minv = [99999]*1000
    qr = n
    x = 0
    k = 0
    ans = 0
    ql = 0
    for i in range(0, q):
        t = input().split(' ')
        s = t[0]
        if s == 'M':
            k = int(t[1])
            x = int(t[2])
            update(1, 1, n)
        else:
            k = int(t[1])
            ql = int(t[2])
            ans = 99999
            query(1, 1, n)
            if ans == 99999:
                print(-1)
            else:
                print(ans)