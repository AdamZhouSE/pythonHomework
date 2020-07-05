nums = eval(input())
count = 0
i = 0
while i < len(nums):
    j = i
    while j < len(nums):
        if max(nums[i: j+1]) == j:
            break
        else:
            j += 1
    count += 1
    i = j+1
print(count)
