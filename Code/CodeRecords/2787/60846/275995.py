def findSteps(nums,permutation):
    steps=0
    for i in range(len(nums)):
        steps+=abs(nums[i]-permutation[i])
    return steps
n=int(input())
nums=[int(x) for x in input().split()]
permutation=[x for x in range(1,n+1)]
for num in nums:
    if num>=1 and num<=n:
        nums.remove(num)
        permutation.remove(num)
nums.sort()
print(findSteps(nums,permutation))