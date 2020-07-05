t = int(input())
for i in range(t):
    n,l,r = [int(x) for x in input().split()]
    ans = n | (2**r-2**(l-1))
    print(ans)