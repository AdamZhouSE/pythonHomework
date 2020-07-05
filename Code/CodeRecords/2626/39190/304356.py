def func34(arr):
    arr=[1]+arr+[1]
    n=len(arr)
    dp=[[0] * n for _ in range(n)]
    for left in range(n-2, -1, -1):
            for right in range(left+2,n):
                dp[left][right] = max(int(arr[left]) * int(arr[i])*int(arr[right])+dp[left][i]+dp[i][right] for i in range(left+1, right))
    return dp[0][n-1]

ip=input().split(",")
op=func34(ip)
print(op)