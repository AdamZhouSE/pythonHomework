def solve():
    n=int(input())
    path=list(map(lambda x:int(x)-1,input().split()))
    edges=[[0 for i in range(n)] for j in range(n)]
    res=[0 for _ in range(n)]
    cur=[]
    for i in range(n-1):
        edge=list(map(int,input().split()))
        edges[edge[0]-1][edge[1]-1]=1
        edges[edge[1]-1][edge[0]-1]=1

    def find(fr,to,p):
        nonlocal cur
        if fr==to:
            cur= p[:-1]
            return
        for ne in range(n):
            if edges[fr][ne]==1 and not (ne in p):
                find(ne,to,p+[ne])

    def putC(p):
        for i in p:
            res[i]+=1

    for i in range(n-1):
        find(path[i], path[i + 1], [path[i]])
        putC(cur)
        
    res=list(map(str,res))
    print('\n'.join(res))

if __name__ == '__main__':
    solve()