def Test():
    f=[]
    d=[]
    ind=[]
    min_tree=[]
    now=[]
    ans=0
    n=int(input())
    for i in range(0,n+1):
        f.append(0)
        d.append(0)
        ind.append(0)
        min_tree.append(0)
        now.append(0)
    for i in range(1,n+1):
        s=input().split()
        f[i]=int(s[0])
        d[i]=int(s[1])
        min_tree[i]=int(s[2])
        if(f[i]!=-1):
            ind[f[i]]+=1
    q=[]
    for i in range(1,n+1):
        if(ind[i]==0):
            q.append(i)
    while (len(q)!=0):
        t=q[0]
        if (d[t] > now[t]):
            ans += min_tree[t] * (d[t]-now[t])
        if (t != 1):
            min_tree[f[t]]=min(min_tree[f[t]], min_tree[t])
            ind[f[t]]-=1
            now[f[t]] += max(d[t], now[t])
            if (ind[f[t]] == 0):
                q.append(f[t])
        q.pop()
    print(ans+2)

if __name__ == "__main__":
    Test()