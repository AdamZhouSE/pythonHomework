A=list(map(int,input().strip().split(",")))
size=len(A)
if size<3:
    print(0)
dp=[0 for _ in range(size-2)]
if A[size-1]-A[size-2]==A[size-2]-A[size-3]:
    dp[size-3]=1
else:
    dp[size-3]=0
for i in range(size-4,-1,-1):
    if A[i+2]-A[i+1]==A[i+1]-A[i]:
        dp[i]=dp[i+1]+1
print(sum(dp))