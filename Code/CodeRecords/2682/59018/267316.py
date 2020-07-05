import math
def changenum(N,L,R):
    a=list(bin(N)[2:])
    for i in range(-R,-L+1):
        a[i]='1'
    print(a)
    
    
    
    
    







T=int(input())
for i in range(T):
    N1,L1,R1=input().split(' ')
    N=int(N1)
    L=int(L1)
    R=int(R1)
    changenum(N,L,R)