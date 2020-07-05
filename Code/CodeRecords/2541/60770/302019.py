def solve():
    n=int(input())
    edges=[[0 for _ in range(n)] for i in range(n)]
    ind=[0 for _ in range(n)]
    src=eval(input())

    for e in src:
        edges[e[1]][e[0]]=1
        ind[e[0]]+=1

    vst=[]
    res=[]
    for i in range(n):
        if ind[i]==0:
            vst.append(i)

    while vst:
        v=vst[0]
        res.append(v)
        del vst[0]
        for i in range(n):
            if edges[v][i]==1:
                edges[v][i]=0
                ind[i]-=1
                if ind[i]==0:
                    vst.append(i)

    if len(res)<n:
        res=[]

    print(res)

if __name__ == '__main__':
    solve()