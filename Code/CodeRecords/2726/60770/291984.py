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

    def isLeaf(p):
        l=lsonOf(p)
        r=rsonOf(p)
        if (l==-1 or tree[l]=='null') and (r==-1 or tree[r]=='null'):
            return True
        return False

    for p in range(len(tree)):
        if isLeaf(p):
            res=int((p+1)**0.5)+1
            print(res)
            return

if __name__ == '__main__':
    solve()
