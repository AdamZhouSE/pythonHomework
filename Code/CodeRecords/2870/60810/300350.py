inp = int(input())
nums = input().split(" ")
oddnums = []
res = 0
for i in range(inp):
    if (int(nums[i]) % 2 == 0):
        res += int(nums[i])
    else:
        oddnums.append(int(nums[i]))
oddnums.sort()
for i in range(1, len(oddnums)):
    res += oddnums[i]
if (len(oddnums) % 2 == 0):
    res += oddnums[0]
print(res)
