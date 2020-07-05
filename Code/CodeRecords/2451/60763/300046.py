nums = eval('['+input()+']')
nums = list(nums)
n = int(input())
if n in nums:
    print(nums.index(n))
else:
    print(0)