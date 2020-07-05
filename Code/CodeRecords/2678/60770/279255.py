def solve():
    n=int(input())
    res=1
    if n==0:
        print(-1)
        return

    while(n>1):
        if n&1!=0:
            print(-1)
            return
        n>>=1
        res+=1
    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()