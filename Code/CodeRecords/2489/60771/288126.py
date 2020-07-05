#08
nums = eval(input())
lower = int(input())
upper = int(input())

count = 0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)+1):
        part = nums[i:j]
        if sum(part) >= lower and sum(part) <= upper:
            count += 1

print(count)