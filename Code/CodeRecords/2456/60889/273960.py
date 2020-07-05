nums = input().strip("[]").split(",")
nums = list(map(int,nums))
counts = []
for i in range(len(nums)):
    count = 0
    for j in range(i+1,len(nums)):
        if nums[j]<nums[i]:
            count = count + 1
    counts.append(count)
print(counts)