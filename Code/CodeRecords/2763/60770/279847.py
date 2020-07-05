def solve():
    m,n=map(int,input().split())

    res=0
    def dfs(st,en,n):
        nonlocal res
        if st>en:
            return
        if n==1:
            res+=(en-st+1)
            return
        for i in range(st,en):
            dfs(i*2,en,n-1)

    dfs(1,m,n)
    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()