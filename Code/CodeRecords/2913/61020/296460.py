def sum_of(a_list):
    pass


n = int(input())
nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

if sum_of(nums) % 2 == 0 and sum_of(nums) - max(nums) >= max(nums):
    print('YES')

else:
    print("NO")
