def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    dp=[0 for x in range(len(nums))]
    index=[-1 for x in range(len(nums))]
    max_len,max_index=0,-1
    for i in range(len(nums)):
        dp[i]=1
        for j in range(i):
            if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
                index[i]=j
            if dp[i]>max_len:
                max_len=dp[i]
                max_index=i
    arr=[]
    while True:
        if max_index!=-1:
            arr.append(nums[max_index])
            max_index=index[max_index]
        else:
            break
    return arr[::-1]

temp=input().split(',')
b=map(eval,temp)
list1=list(b)
list1.sort()
ans=largestDivisibleSubset(list1)
print(ans)
