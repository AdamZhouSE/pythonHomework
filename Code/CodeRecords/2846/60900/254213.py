n = input()
str = input()
nums = str.split(" ")
nums = list(set(nums))
count = 0
for i in range(0,len(nums)):
    if(nums[i]=='0'):
        count = count+1

print(len(nums)-count)