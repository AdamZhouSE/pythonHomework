line = input()
nums = line.split(',')
f = []
for i in range(len(nums)):
    nums[i] = int(nums[i])
    f.append(1)
for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            f[i] = max(f[i], f[j] + 1)
print(max(f))
