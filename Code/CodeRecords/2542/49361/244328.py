arrays = input().replace("[", "").replace("]", "").split(",")
nums = []
for each in arrays:
    each = int(each)
    nums.append(each)
nums = set(nums)
res = 0
for i in nums:
    if i - 1 not in nums:
        y = i + 1
        while y in nums:
            y += 1
        res = max(res, y - i)
print(res)
