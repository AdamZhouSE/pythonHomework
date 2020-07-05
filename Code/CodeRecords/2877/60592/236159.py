num = int(input())
nums = input().split(' ')
for i in range(0,num):
    nums[i] = int(nums[i])
sum = 0
for i in range(0,num):
    if nums[i]>0:
        sum+=nums[i]
    else:
        sum-=nums[i]
print(sum)