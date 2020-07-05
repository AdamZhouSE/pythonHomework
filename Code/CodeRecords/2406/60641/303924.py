n = int(input().strip())
nums = [0 for i in range(0, n)]
for i in range(0, n):
    nums[i] = int(input().strip())
sorted_nums = sorted(nums)

x, y = -1, -1
gap = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        gap_1 = abs(i - sorted_nums.index(nums[i])) + abs(j - sorted_nums.index(nums[j]))
        gap_2 = abs(j - sorted_nums.index(nums[i])) + abs(i - sorted_nums.index(nums[j]))
        if gap_1 - gap_2 > gap:
            x = i
            y = j

temp = nums[y]
nums[y] = nums[x]
nums[x] = temp

result = 0
for i in range(0, n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = nums[j]
            result += 1
print(result)
