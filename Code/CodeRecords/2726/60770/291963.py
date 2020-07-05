def solve():
    tree=input()[1:-1].split(',')
    res=float('inf')

    def lsonOf(fa):
        fa += 1
        fa *= 2
        fa -= 1
        if fa>=len(tree):
            return -1
        return fa

    def rsonOf(fa):
        res=lsonOf(fa) + 1
        if res==0:
            return -1
        return res

    def dfs(cur,path):
        nonlocal res
        l=lsonOf(cur)
        r=rsonOf(cur)
        if (l==-1 or tree[l]=='null') and (r==-1 or tree[r]=='null'):
            res=min(cur+1,res)
            return
        if l!=-1 and tree[l]!='null':
            dfs(l,path+1)
        if r!=-1 and tree[r]!='null':
            dfs(r,path+1)

    dfs(0,0)
    print(res)

if __name__ == '__main__':
    solve()
