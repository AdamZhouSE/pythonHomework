import math
def changenum(N,L,R):
    n=N+math.pow(2,L-1)+math.pow(2,R-1)
    print(int(n))
    
    
    
    







T=int(input())
for i in range(T):
    N1,L1,R1=input().split(' ')
    N=int(N1)
    L=int(L1)
    R=int(R1)
    changenum(N,L,R)