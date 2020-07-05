T=int(input())
n=[]
A=[[0]*int(n**0.5)]*n
for i in range(0,T):
    n.append(int(input()))
    for j in range(0,n[i]**2):
        A[i]=list(int(input().split()))
for i in range(0,T):
    #将每行数组打印成n*n
    for j in range(0,n[i]**2):
        b=[[1]*n[i]]*n[i]
        for m in range(0,n[i]):
            b[m].append(A[i][])
            
        
        