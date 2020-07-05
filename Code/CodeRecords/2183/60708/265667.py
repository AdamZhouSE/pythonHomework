N=int(input())
for n in range(0,N):
    K=int(input())
    x = 2 * K
    if K==1:
        K=1
    else:
        K=K*K-(K-1)
    result=0
    for i in range(0,x):
        result=result+K
        K=K+1
    print(result)