def solve():
    n=int(input())
    mnys=[]
    for i in range(n):
        mnys.append(int(input()))

    def minV(t):
        res=float('inf')
        if t==0:
            return mnys[t]
        for i in range(t):
            res=min(abs(mnys[i]-mnys[t]),res)
        return res

    res=0
    for t in range(n):
        res+=minV(t)
    print(res,end='')

if __name__ == '__main__':
    solve()