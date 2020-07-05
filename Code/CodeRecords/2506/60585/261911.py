arr=list(map(int,input().strip().split(',')))
n=len(arr)
dp=[1 for _ in range(n)]
maxL=1
for i in range(1,n):
    temp=0
    for j in range(i):
        if arr[i]>arr[j]:
            temp=max(temp,dp[j])
    dp[i]=temp+1
    maxL=max(maxL,dp[i])
print(maxL)