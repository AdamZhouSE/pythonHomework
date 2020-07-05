n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i] = int(nums[i])
count =0
for i in range(0,n):
    while (nums.count(nums[i])>1):
        nums[i]+=1
        count+=1
print(count)