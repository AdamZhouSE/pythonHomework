def P(N):
    if n>=3:
        return P(N-2)+P(N-3)
    else:
        return 1
    


T=int(input())
for i in range(T):
    N=int(input())
    print(P(N))
    