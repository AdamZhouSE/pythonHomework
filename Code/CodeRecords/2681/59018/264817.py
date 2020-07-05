def smalldo(N):
    count=0
    while N!=0:
        if N%2==0:
            N=N//2            
        else:
            N=N-1
        count=count+1    
    print(count)
    
    
    
T=int(input())
for i in range(T):
    N=int(input())
    smalldo(N)