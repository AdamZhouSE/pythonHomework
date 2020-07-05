def find_min(nums:list):
    result = int(pow(2,31))
    for i in range(len(nums)):
        if nums[i] < result:
            result = nums[i]
    return result

def do(nums):
    if len(nums) <= 2:
        return -1
    leftMax = nums[0]
    rightMin = find_min(nums[2:])
    for i in range(1,len(nums)-1):
        if leftMax <= nums[i] <= rightMin:
            return nums[i]
        else:
            leftMax = max(leftMax,nums[i])
            rightMin = find_min(nums[i+1:])
    return -1


T = int(input())

for t in range(T):
    size = int(input())
    nums = [int(n) for n in input().split(' ')]
    print(do(nums))