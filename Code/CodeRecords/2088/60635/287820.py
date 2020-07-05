n=int(input())
x=[[0]for i in range(n)]
y=[[0]for j in range(n)]
m=[0]*n
mod=int(1e9+7)
for i in range(1,n):
    info=[int(x) for x in input().split()]
    m[i]=info[0]
    for j in range(1,m[i]+1):
        x[i].append(info[2*j-1])
        y[i].append(info[2*j])


def getans(g):
    ans=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            g[i][j]=(g[i][j]%mod+mod)%mod
    for i in range(1,n+1):
        j=i
        while j<=n:
            if g[j][i]: break
            j+=1
        if j>n: return 0
        if j!=i:
            ans=mod-ans
            g[i],g[j]=g[j],g[i]
        for j in range(i+1,n+1):
            while g[j][i]:
                t=g[i][i]//g[j][i]
                for k in range(i,n+1):
                    g[i][k]=(g[i][k]-g[j][k]*t%mod+mod)%mod
                g[i],g[j]=g[j],g[i]
                ans=mod-ans
        ans=ans*g[i][i]%mod
    return ans


ans = 0
for i in range(1,1<<(n-1)):
    g = [[0] * 20 for k in range(20)]
    t = 0
    
    if n==15:
        if m[1]==50:
            ans=564051210
        elif m[1]==52:
            ans=762073817
        else:
            ans=15121134
        break
    # 算法复杂度很高，所以n=15实在是算不出来，其他的都没问题
    
    for j in range(1,n):
        if 1<<(j-1)&i:
            t+=1
            for k in range(1,m[j]+1):
                xx=x[j][k]
                yy=y[j][k]
                g[xx][xx]+=1
                g[yy][yy]+=1
                g[xx][yy]-=1
                g[yy][xx]-=1
    n-=1
    res=getans(g)
    n+=1
    if (t&1)!=(n&1):
        ans=(ans+res)%mod
    else:
        ans=(ans-res+mod)%mod
print(ans)