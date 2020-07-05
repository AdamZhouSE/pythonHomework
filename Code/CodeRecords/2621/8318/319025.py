es = input().split(',')
nums = list(map(int, es))
tmp = nums[0]
max_ = tmp
n = len(nums)
for i in range(1,n):
    if tmp + nums[i]>nums[i]:
        max_ = max(max_, tmp+nums[i])
        tmp = tmp + nums[i]
    else:
        max_ = max(max_, tmp, tmp+nums[i], nums[i])
        tmp = nums[i]
print(max_)