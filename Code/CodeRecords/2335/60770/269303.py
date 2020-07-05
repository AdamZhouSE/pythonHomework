import math

def solve():
    n=int(input())
    m=int(input())
    if m<=n:
        print(n-m)
        return
    res=1
    while m>2*n:
        res+=1
        n*=2
    res+=math.ceil((2*n-m)/2)
    print(res)

if  __name__ == '__main__' :
    solve()