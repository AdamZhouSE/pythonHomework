size=int(input())
nums=list(map(int,input().split(' ')))
sequence=list(map(int,input().split(' ')))
nums.insert(0,0)
dp=[0 for i in range(size+1)]
dp[1]=nums[1]
for i in range(2,size+1):
    dp[i]=dp[i-1]+nums[i]
for index in sequence:
    for i in range(index+1,size+1):
        if(dp[i]==0):
            break
        dp[i]-=dp[index]
    dp[index]=0
    maxsize=max(dp)
    print(maxsize)


