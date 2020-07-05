def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)
T=int(input())
for i in range(T):
    n=int(input())
    print(lucas(n)%1000000007)