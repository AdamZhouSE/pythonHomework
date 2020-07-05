def solve():
    n=int(input())
    srcs=list(map(lambda x:list(map(int,x.strip('[').strip(']').split(','))),(input()[1:-1].split('],['))))
    src=int(input())
    dst=int(input())
    k=int(input())

    edges=[[-1 for i in range(n)] for i in range(n)]
    for s in srcs:
        edges[s[0]][s[1]]=s[2]

    minCost=99999
    def dfs(fr,to,cost,path):
        nonlocal minCost
        if fr==to:
            if cost<minCost:
                minCost=cost
            return
        if path==0:
            return

        cango=[]
        for i in range(n):
            if edges[fr][i]>=0:
                cango.append(i)
        for des in cango:
            dfs(des,to,cost+edges[fr][des],path-1)

    dfs(src,dst,0,k+1)
    if minCost==99999:
        minCost=-1
    print(minCost)



if __name__ == '__main__':
    solve()