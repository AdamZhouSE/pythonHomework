nums = eval(input())
counts = []
for i in range(len(nums)):
    c = 0
    for j in range(len(nums)-1):
        if nums[j+1] < nums[j]:
            c += 1
    counts.append(c)
print(counts)
