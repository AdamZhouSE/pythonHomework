inp = input()
tmp = inp[1:len(inp) - 1].split(',')
nums = [int(tmp[i]) for i in range(len(tmp))]
res = 0
for i in range(0, len(nums) - 1):
    for j in range(i, len(nums)):
        if nums[i] > 2 * nums[j]:
            res += 1
print(res)
