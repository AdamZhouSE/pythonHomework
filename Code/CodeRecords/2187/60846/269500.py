T=int(input())
while T:
    basicInfo=[int(x) for x in input().split()]
    K=basicInfo[1]
    nums=[int(x) for x in input().split()]
    tmpSum=0
    for i in range(K):
        tmpSum+=nums[i]
    maxSum=tmpSum
    for i in range(K,len(nums)):
        tmpSum=tmpSum-nums[i-K]+nums[i]
        maxSum=max(maxSum,tmpSum)
    print(maxSum)
    T-=1