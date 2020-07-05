n = 0
a = [0]*100
b = [0]*100
f = [0]*100
sum = [0]*100
ans = [0]*100
num = 0
maxx = 0
def father(x):
    if x == f[x]:
        return x
    f[x] = father(f[x])
    return f[x]

if __name__=='__main__':
    n = eval(input())
    line = input().split(' ')
    for i in range(1,n+1):
        a[i] = int(line[i-1])
    line = input().split(' ')
    for i in range(1,n+1):
        b[i] = int(line[i-1])
    for i in range(n,0,-1):
        now = b[i]
        if f[now] == 0:
            f[now] = now
            sum[now] = a[now]
        fnow = father(now)
        if f[now-1]!=0 and now-1>0:
            f1 = father(now-1)
            if fnow!=f1:
                sum[now]+=sum[f1]
                sum[f1] = 0
                f[f1] = now
        if f[now+1]!=0 and now+1<=n:
            fr = father(now+1)
            if fnow!=fr:
                sum[now]+=sum[fr]
                sum[fr] = 0
                f[fr] = now
        maxx = max(maxx,sum[now])
        num = num + 1
        ans[num] = maxx
    for i in range(n-1,0,-1):
        print(ans[i])
    print(0)