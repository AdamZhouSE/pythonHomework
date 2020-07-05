n = eval(input())
nums = input().split(" ")
number = 1
count = 1
i = 0
for i in range(len(nums)):
    if(nums[i] != '0'):
        break
while(i < len(nums)):
    if(nums[i] == '1'):
        number *= count
        count = 1
    else:
        count += 1
    i = i + 1
print(number)