maxn = 100001
nxt, head, k, size, b, mx, n, root, top, T = [0]*(2*maxn), [0]*maxn, 0, [0]*maxn, [0]*(2*maxn), [0]*maxn, 0, 0, [0]*maxn, 0
siz = [[0 for i in range(2)] for i in range(maxn)]


def push(s, t):
    global nxt, head, k
    k += 1
    nxt[k] = head[s]
    head[s] = k
    b[k] = t
    
    
def getr(x, f):
    global size, head, nxt, b, mx, root
    size[x] = 1
    i = head[x]
    while i:
        if b[i] != f:
            getr(b[i], x)
            size[x] += size[b[i]]
            mx[x] = max(mx[x], size[b[i]])
        i = nxt[i]
    mx[x] = max(mx[x], n - size[x])        
    if mx[x] < mx[root]:
        root = x
        
        
def dfs(x, f):
    global size, head, nxt, top
    size[x] = 1
    i = head[x]
    while i:
        if b[i] != f:
            top[b[i]] = top[x] if top[x] else b[i]
            dfs(b[i], x)
            size[x] += size[b[i]]
        i = nxt[i]
            
            
if __name__ == "__main__":
    n, k = map(int, input().split())
    for i in range(n-1):
        u, v = map(int, input().split())
        push(u, v)
        push(v, u)
    root = 0
    mx[root] = n
    getr(1, 0)
    dfs(root, 0)
    summ, cnt = n, 0
    i = head[root]
    while i:
        T += 1
        siz[T][0], siz[T][1] = size[b[i]], b[i]
        i = nxt[i]
    if T <= k+1:
        for i in range(n):
            print(1)
    else:
        siz.sort()
        skd = [0, 0]
        for i in range(1, T+1):
            if siz[i] >= siz[T-k+1]:
                cnt += 1
                summ -= siz[i][0]
            else:
                skd = max(skd, siz[i])
        for i in range(1, n+1):
            if i==root:
                print(1)
            else:                
                b1 = 1 if [size[top[i]], top[i]] >= siz[T-k+1] else 0
                b2 = 1 if [size[top[i]]-size[i], top[i]] >= siz[T-k+1] else 0
                b3 = 1 if [size[top[i]]-size[i], top[i]] >= skd else 0
                newval = summ
                if (not b1) and (not b2):
                    newval -= size[i]
                if (not b1) and b2:
                    newval = newval - size[top[i]] + size[T-k+1][0]
                if b1 and (not b3):
                    newval = newval -skd[0] + size[top[i]] - size[i]
                print(1 if newval<=(n>>1) else 0)
