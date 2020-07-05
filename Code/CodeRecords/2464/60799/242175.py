s, nums = int(input()), [int(i) for i in input().split(',')]
res, current = len(nums) + 1, nums[0]
left, right = 0, 1
while left != len(nums) - 1:
    if current >= s:
        res = min(right - left, res)
        current -= nums[left]
        left += 1
    elif right < len(nums):
        current += nums[right]
        right += 1
    else:
        break
print(res)
