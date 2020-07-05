def solve():
    n,q=map(int,input().split())
    kids=[[_,float('inf')] for _ in range(1,n+1)]
    for i in range(q):
        op=input().split()
        if op[0]=='M':
            a=int(op[2])
            x=int(op[1])
            kids[a-1][1]=x
        elif op[0]=='D':
            y=int(op[1])
            b=int(op[2])
            ks=kids[b-1:]
            res=-1
            for k in ks:
                if k[1]<=y:
                    res=k[0]
                    break
            print(res)


if __name__ == '__main__':
    solve()