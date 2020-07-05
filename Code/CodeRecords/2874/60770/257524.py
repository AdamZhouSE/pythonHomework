def solve():
    n=int(input())
    states=list(map(int,input().split()))
    res=255

    def dfs(index,last,rest):
        nonlocal res
        if index==n:
            if rest<res:
                res=rest
            return
        if states[index]==0:
            dfs(index+1,0,rest+1)
        elif states[index]==3:
            if last==1:
                dfs(index+1,2,rest)
            elif last==2:
                dfs(index+1,1,rest)
            else:
                dfs(index+1,1,rest)
                dfs(index+1,2,rest)
        elif states[index]==1:
            if last==1:
                dfs(index+1,0,rest+1)
            else:
                dfs(index+1,1,rest)
        else:
            if last==2:
                dfs(index+1,0,rest+1)
            else:
                dfs(index+1,2,rest)

    dfs(0,0,0)
    print(res)

if  __name__ == '__main__' :
    solve()