carr=input().split(",")
arr=[]
for i in carr:
    i=int(i)
    arr.append(i)
dif=int(input())
count=1
res=1
dp=[0 for i in range(100)]
for i in range(len(arr)-1,-1,-1):
    if arr[i]+dif<0 or arr[i]+dif>20000:
        dp[arr[i]]=1
    dp[arr[i]]=dp[arr[i]+dif]+1
    res=max(res,dp[arr[i]])
print(res)   