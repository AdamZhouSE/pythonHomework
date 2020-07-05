n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i] = int(nums[i])
for i in range(0,n-1):
    if i%2 ==0:
        del nums[nums.index(max(nums))]
    else:
        del nums[nums.index(min(nums))]
print(nums[0])