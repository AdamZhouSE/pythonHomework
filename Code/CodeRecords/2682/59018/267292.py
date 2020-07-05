import math
def changenum(N,L,R):
    num=0
    for i in range(L-1,R):
        num=num+math.pow(2,i)
    N=N+num
    print(int(N))
    
    
    
    







T=int(input())
for i in range(T):
    N1,L1,R1=input().split(' ')
    N=int(N1)
    L=int(L1)
    R=int(R1)
    changenum(N,L,R)