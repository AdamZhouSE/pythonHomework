def changenum(N,L,R):
    n=list(bin(N))
    n[-L]=1
    n[-R]=1
    print(n)
    
    
    







T=int(input())
for i in range(T):
    N1,L1,R1=input().split(' ')
    N=int(N1)
    L=int(L1)
    R=int(R1)
    changenum(N,L,R)