n = eval(input())
nums = sorted(list(set(list(map(int, input().split(' '))))))
print('YES') if len(nums)==1 or len(nums)==3 and nums[2] - nums[1] == nums[1] - nums[0] else print('NO')