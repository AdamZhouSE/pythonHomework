nums = eval(input())
count = 0
total = 0
for i in range(len(nums)):
    total += nums[i]
    if total == i*(i+1)/2:
        count += 1
print(count)