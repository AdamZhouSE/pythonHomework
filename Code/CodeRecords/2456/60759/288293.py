nums = eval(input())
counts = []
for i in range(len(nums)):
    counts.append(len([n for n in nums[i + 1:] if n < nums[i]]))
print(counts)
