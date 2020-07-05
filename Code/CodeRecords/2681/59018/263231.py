import math
def smallest(N):
    count=1
    if N%2==0:        
        while N>1:
            N=N/2
            count=count+1
    else:        
            count=count+2
            N=math.floor(N/2)
            while N>1: 
                if N%2!=0:
                    count=count+2
                else:
                    count=count+1
    return count           
                
                
        





T=int(input())
for i in range(T):
    N=int(input())
    print(smallest(N))