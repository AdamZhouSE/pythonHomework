A=input().split(",")
for i in range(len(A)):
    A[i]=int(A[i])
K=int(input())
n=len(A)
A=sorted(A)        
res=A[n-1]-A[0]        
for i in range(1,n):            
    small=min(A[0]+K,A[i]-K)            
    large=max(A[i-1]+K,A[n-1]-K)            
    res=min(res,large-small)
print(res)