from collections import defaultdict
def tree_diametre():
    n=int(input())
    g,ans=defaultdict(list),0
    l=[]
    for i in range(n-1):
        x,y=map(int,input().split())
        l.append([x,y])
        g[x].append(y)
        g[y].append(x)

    def dfs(cur,pre):
        nonlocal ans
        d1=d2=0
        for i in g[cur]:
            if i!=pre:
                d=dfs(i,cur)
                if d>d1:
                    d1,d2=d,d1
                elif d>d2:
                    d2=d
        ans=max(ans,d1+d2)
        return d1+1

    dfs(l[0][0],None)
    return ans


print(tree_diametre())