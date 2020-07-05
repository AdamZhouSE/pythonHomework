def inorder(nums):
    if len(nums) == 1:
        return True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

T = int(input())
for t in range(T):
    x = int(input())
    nums = [int(z) for z in input().split(' ') ]
    begin = 0
    end = 0
    ebegin = nums[begin]
    eend = nums[end]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if inorder(nums[i:j+1]) and j-i > end-begin:
                begin = i
                ebegin = nums[i]
                end = j
                eend = nums[j]
    print(2**(x-3))