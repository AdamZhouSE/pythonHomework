nums = input()[1:-1].split(',')
k = int(input())
for i in range(0, len(nums)):
    nums[i] =int(nums[i])
n = len(nums)

result =-1

if k <nums[0] or k>nums[n-1]:
    result =-1

else:
    for i in range(0,n):
        if k ==nums[i]:
            result = i

print(result)