nums = eval(input())
while len(nums) != 1:
    n = nums[0]
    nums.remove(n)
    if n not in nums:
        nums = [n]
        break
    else:
        nums.remove(n)
print(nums[0])