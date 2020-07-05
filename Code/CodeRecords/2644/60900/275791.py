import math
nums = input()[1:-1].split(',')
K = int(input())
for i in range(0, len(nums)):
    nums[i] =int(nums[i])
n = len(nums)

result = 999
for i in range(0,n):
    temp =i
    count =0
    while count <K and temp!=n:
        count +=nums[temp]
        temp+=1
    if temp-i <result and count >=K:
        result = temp-i

if result ==999:
    result =-1

print(result)