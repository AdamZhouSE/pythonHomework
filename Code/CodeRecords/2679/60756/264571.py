T=int(input())
for t in range(T):
    N=int(input())
    if N>=3:
        print(1+2*N+(3*N*(N-1)//2)+(N*(N-1)*(N-2)//2))
    elif N==2:
        print(8)
    elif N==1:
        print(3)
    else:
        print(0)