nums = [int(i) for i in input().split(',')]
nums.insert(0, float('-Inf'))
n = len(nums)
nums.append(float('-Inf'))
for i in range(1, n):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        print(i-1)
        break