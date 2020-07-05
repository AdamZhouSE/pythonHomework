
def dfs(x,z):
    if v[x]!=0:
        if u[x]==now:
            maxx=min(maxx,z-v[x])
        return
    u[x]=now
    v[x]=z
    dfs(a[x],z+1)
    return
def main():
    v=[]
    u=[]
    maxx=1000
    n=int(input())
    a=[int(k) for k in input().split()]
    a.insert(0,0)
    for i in range(1,n+1):
        now=i
        if v[i]==0:
            u[i]=now
            v[i]=1
            dfs(a[i],2)
    print(maxx)
    return 0;
    
if __name__=='__main__':
    main()
        