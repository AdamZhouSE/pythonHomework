n = int(input())
nums = []
for i in range(n):
    nums.append(input().split())
count = 0
for x in range(n):
    for y in range(x + 1, n):
        if nums[x][0] == nums[y][0] or nums[x][1] == nums[y][1]:
            count += 1
print(count)
