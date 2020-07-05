T=int(input())
for k in range(T):
    N=int(input())
    result=0
    while N!=0:
        if N%2==1:
            N-=1
            result+=1
        else:
            N/=2
            result+=1
    print(result)