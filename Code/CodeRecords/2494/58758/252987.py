s = input()
nums = [int(x) for x in s[1: len(s)-1].split(',')]
count = 0
for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j] * 2:
            count += 1
print(count)
