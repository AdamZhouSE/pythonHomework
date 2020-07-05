def func4(arr):
    if len(arr)==0:
        print("0")
    elif len(arr)==1:
        print(arr[0])
    else:
        dp=[0]*len(arr)
        ans=dp[0]=int(arr[0])
        for i in range(1,len(arr)):
            dp[i]=max(dp[i-1],0)+int(arr[i])
            ans=max(ans,dp[i])
        print(ans)
ip=input().split(",")
func4(ip)