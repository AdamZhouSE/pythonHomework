arr = input()[1:-1]
nums = [int(i) for i in arr.split(',')]
nums.sort()
if len(nums)<2:
    print('0')
    exit()
for i in range(len(nums)-1):
    nums[i] = abs(nums[i] - nums[i+1])
nums.pop(-1)
print(max(nums))