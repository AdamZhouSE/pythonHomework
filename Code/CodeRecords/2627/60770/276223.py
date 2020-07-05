def solve():
    l,s=map(int,input().split())
    a=(l-(l**2-24*s)**0.5)/12
    v=a*(s/2-a*(l/4-a))
    print("%.5f"%v)

if  __name__ == '__main__' :
    n=int(input())
    for i in range(n):
        solve()