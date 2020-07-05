arr=eval(input())
maxL=0
dp=dict()
for num in arr:
    if num not in dp:
        left=dp.get(num-1,0)
        right=dp.get(num+1,0)
        temp=1+left+right
        maxL=max(maxL,temp)
        dp[num]=maxL
        dp[num-left]=maxL
        dp[num+right]=maxL
print(maxL)