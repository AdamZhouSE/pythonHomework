T=int(input())
for i in range(T):
    N=int(input())
    n0=N*(N-1)+1
    nn=N*(N+1)
    res=(n0+nn)*N
    print(res)