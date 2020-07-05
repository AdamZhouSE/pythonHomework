def minSubset(s, nums):
    if not nums:
        return 0
    li = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)+1):
            if sum(nums[i:j]) >= s:
                li.append(len(nums[i:j]))
    if len(li) == 0:
        return 0
    else:
        return min(li)
s=int(input())
nums=list(map(int,input().split(',')))
print(minSubset(s,nums))