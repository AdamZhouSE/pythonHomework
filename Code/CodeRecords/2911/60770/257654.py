def solve():
    n,m=map(int,input().split())
    gold=list(map(int,input().split()))
    root=[-1 for i in range(n)]

    def rootOf(a):
        if root[a]==-1:
            return a
        return rootOf(root[a])

    def combin(a,b):
        root1=rootOf(a)
        root2=rootOf(b)
        if root1==root2:
            return
        g=min(gold[root1],gold[root2])
        root[root2]=root1
        gold[root1]=g

    def getSum():
        res=0
        for i in range(n):
            if root[i]==-1:
                res+=gold[i]
        return res

    for i in range(m):
        a,b=map(int,input().split())
        combin(a-1,b-1)

    print(getSum())

if  __name__ == '__main__' :
    solve()