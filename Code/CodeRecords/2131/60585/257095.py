A=list(map(int,input().strip().split(',')))
dp=0
n=len(A)
res=0
for i in range(2,n):
    if A[i]-A[i-1]==A[i-1]-A[i-2]:
        dp+=1
        res+=dp
    else:
        dp=0
print(res)