def dp(n:int,N:int,x:int):
    if n==N:
        return x
    elif n>N:
        return float("Inf")
    elif n==0:
        return dp(n+1,N,x+1)
    else:
        return min(dp(n+1,N,x+1),dp(n*2,N,x+1))

T=int(input())
for t in range(T):
    N=int(input())
    print(dp(0,N,0))