def solve():
    n=int(input())

    resset=set()
    comb=(0,0,0)

    def dfs(n,comb):
        if n<3:
            if n==0:
                if comb not in resset:
                    resset.add(comb)
            return
        dfs(n-3,(comb[0]+1,comb[1],comb[2]))
        dfs(n - 5, (comb[0], comb[1]+1, comb[2]))
        dfs(n - 10, (comb[0], comb[1], comb[2]+1))

    dfs(n,comb)
    print(len(resset))

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()