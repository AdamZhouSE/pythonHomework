nums = eval(input())
l = len(nums)
count = 0
for i in range(l-1):
    for j in range(i+1, l):
        if nums[i]>2*nums[j]:
            count += 1
print(count)
