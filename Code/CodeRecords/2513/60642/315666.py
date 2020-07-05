times = int(input())
str=''
for i in range(times):
    str=str+input()+','
str = str[0:-1]
nums = [int(i) for i in str.split(',')]
nums.sort()
k = int(input())
print(nums[k-1])