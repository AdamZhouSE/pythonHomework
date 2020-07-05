def P(n):
    if n==0 or n==1 or n==2:
        return 1
    else:
        return P(n-2)+P(n-3)
T=int(input())
for i in range(T):
    N=int(input())
    print(P(N))