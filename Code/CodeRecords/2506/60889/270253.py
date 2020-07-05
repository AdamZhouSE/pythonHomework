nums = input().split(",")
nums = list(map(int,nums))
LIS = []
for i in range(len(nums)):
    length = 0
    for j in range(i):
        if nums[i] > nums[j]:
            if length < LIS[j]:
                length = LIS[j]
    length = length + 1
    LIS.append(length)
longest = 0
for i in LIS:
    if i > longest:
        longest = i
print(longest)