def sum_of(a_list):
    pass


n = int(input())
nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

if sum(nums) % 2 == 0 and sum(nums) - max(nums) >= max(nums):
    print('YES')

else:
    print("NO")
