import math
str = input().split(',')
nums =[]
for i in range(0,len(str)):
    nums.append(int(str[i]))

n = len(nums)
nums = list(set(nums))
result = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        result = result+ (nums[j]-nums[i])*(2**(j-i-1))
print(result)