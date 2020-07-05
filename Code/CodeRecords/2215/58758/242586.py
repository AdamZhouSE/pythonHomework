nums = input().split(',')
if len(nums) == 1:
    print(nums[0])
elif len(nums) == 2:
    print(nums[0] + '/' + nums[1])
else:
    ans = nums[0] + '/('
    for i in range(1, len(nums)-1):
        ans += nums[i] + '/'
    ans += nums[len(nums)-1] + ')'
    print(ans)
