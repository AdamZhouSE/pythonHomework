n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i]= int(nums[i])
print(max(nums))