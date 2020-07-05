def f(n):
    if(n<=1): return 1
    return n*f(n-1)

t=int(input())
while t>0:
    t-=1
    n,m,l,r=input().split()
    n=int(n)
    m=int(m)
    l=int(l)
    r=int(r)
    ans=f(n+m)
    #print(n,m,l,r)
    a=input().split()
    a=list(map(int,a))
    #print(a)
    rec=[0]*10000
    vis=[0]*10000
    for i in range(n):
        rec[a[i]]+=1
    for i in range(l,r+1): 
        #rec[i]=a.count(i)
        m+=rec[i]
    p=r-l+1
    ave=int(m/p)
    #cont=[ave]*(r-l+1)
    for i in range(l,r+1):
        if(rec[i]>ave):
            m-=rec[i]
            p-=1
    ave=int(m/p)
    rest=m%p
    for i in range(l,r+1):
        if(rec[i]<ave): rec[i]=ave
        if(rest>0):
            rec[i]+=1
            rest-=1
    #print(ans)
    for i in range(n):
        if(vis[a[i]]==0):
            vis[a[i]]=1
            ans=int(ans/f(rec[a[i]]))
    for i in range(l,r+1):
        if(vis[i]==0):
            vis[i]=1
            ans=int(ans/f(rec[i]))
    print(ans)
