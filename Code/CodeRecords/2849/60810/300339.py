inp = int(input())
nums = input().split(" ")
for i in range(inp):
    nums[i] = int(nums[i])

res = -1
for i in range(inp):
    res = nums[i]
    for j in range(inp):
        if (nums[j] % nums[i] != 0):
            res = -1
            break
    if (res != -1):
        break
print(res)