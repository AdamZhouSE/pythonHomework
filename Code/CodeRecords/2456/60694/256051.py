nums = eval(input())
counts = []
for i in range(len(nums)-1):
    c = 0
    for j in range(i+1, len(nums)):
        if nums[j] < nums[i]:
            c += 1
    counts.append(c)
counts.append(0)
print(counts)
