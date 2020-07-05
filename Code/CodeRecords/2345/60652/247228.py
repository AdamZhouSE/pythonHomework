def find():
    N=int(input())
    a=list(map(int,input().split()))
    A=0
    B=0
    num=[]
    a.sort()
    for i in range(1,N+1):
        if not i in a:
            A=i
            break
    for i in range (0,N-1):
        if a[i]==a[i+1]:
            B=a[i]
    print(B,A)
    
    
T=int(input())
for i in range(0,T):
    find()
            