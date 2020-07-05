def dfs(p,q,now):
    global x,y,res
    d = abs((len(x)-p)-(len(y)-q))
    if now+d>=res:
        return
    while p<len(x) and q<len(y) and x[p]==y[q]:
        p += 1
        q += 1
    if p==len(x):
        res = min(res,now+len(y)-q)
        return
    if q==len(y):
        res = min(res,now+len(x)-p)
        return
    dfs(p+1,q,now+1)
    dfs(p,q+1,now+1)
    dfs(p+1,q+1,now+1)
    return

n = int(input())
a = []
ans = [0]*8
for t in range(n):
    a.append(input())
for i in range(n):
    for j in range(i+1,n):
        if abs(len(a[i])-len(a[j]))<=8:
            res = 9
            x = a[i]
            y = a[j]
            dfs(0,0,0)
            if res-1<8 and res-1>=0:
                ans[res-1] += 1
for i in range(8):
    ans[i] = str(ans[i])
print(' '.join(ans),'',end='')