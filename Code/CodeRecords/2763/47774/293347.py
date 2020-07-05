def solve(m,n):
    if m<n:
        return 0
    if n==0:
        return 1
    res=solve(m-1,n)+solve(m//2,n-1)
    return res

num=int(input())
for nn in range(num):
    m,n=input().split(' ')
    m,n=int(m),int(n)
    print(solve(m,n))
    