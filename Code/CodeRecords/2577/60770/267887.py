def solve():
    startTime=list(map(int,input().split(',')))
    endTime=list(map(int,input().split(',')))
    reward=list(map(int,input().split(',')))
    n=len(startTime)
    res=0

    def isConflict(i,j):
        if endTime[i]<=startTime[j] or endTime[j]<=startTime[i]:
            return False
        return True

    def isC(i,p):
        for w in p:
            if isConflict(i,w):
                return True
        return False

    def dfs(start,path):
        nonlocal res
        ok=[]
        if not path:
            ok=list(range(n))
        else:
            for i in range(start,n):
                if not isC(i,path):
                    ok.append(i)
        if not ok:
            res=max(sum(map(lambda x:reward[x],path)),res)
        else:
            for work in ok:
                dfs(work+1,path+[work])

    dfs(0,[])
    print(res)

if  __name__ == '__main__' :
    solve()