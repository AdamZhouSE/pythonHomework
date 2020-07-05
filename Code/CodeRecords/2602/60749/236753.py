nums=input()

nums=nums[1:len(nums)-1]
numA=list(map(int, nums.split(",")))
nums2=input()
nums2=nums2[1:len(nums2)-1]
numB=list(map(int, nums2.split(",")))
res=[]
dp=[]
max1=0
for x in range(0,len(numB)):
    res.append(0)
for x in range(0, len(numA)):
    dp.append(res)
for x in range(0,len(numB)):
    if numA[0]==numB[x]:
        dp[0][x]=1
for x in range(0,len(numA)):
    if numB[0]==numA[x]:
        dp[x][0]=1

for i in range(1,len(numA)):
    for j in range(1,len(numB)):
        if numA[i]==numB[j]:
            dp[i][j]=dp[i-1][j-1]+1
            max1=max(dp[i][j], max1)
print(max1)   