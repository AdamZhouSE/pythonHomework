def largest(nums):
    n=len(nums)
    sum=0
    sum0=0
    for i in range(n):
        sum=sum+nums[i]
    for i in range(n):
        for j in range(i,n):
            sum0=sum0+nums[j]
            if sum0>sum:
                sum=sum0
            elif j==n-1:
                sum0=0
            else:
                pass
    return sum
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(largest(nums))