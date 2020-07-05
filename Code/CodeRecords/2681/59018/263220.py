def smallest(N):
    count=0
    if N%2==0:        
        while N>1:
            N=N/2
            count=count+1
    else:
        while N>1:
            count=count+2
            N=floor(N/2)
            if N>1 and N%2!=0:
                count=count+2
            elif N>1 and N%2==0:
                count=count+1
    return count           
                
                
        





T=int(input())
for i in range(T):
    N=int(input())
    print(smallest(N))