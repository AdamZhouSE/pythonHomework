def satic(fir, nums, inp, sum1):
    if (nums[inp - 1] == 1): sum1 -= 1
    res = []
    temp = 1
    for i in range(fir + 1, inp):
        if (nums[i] == 1):
            res.append(temp)
            temp = 1
        else:
            temp += 1
    return (res)


def cuting(nums, inp):
    sum1 = 1
    res=1
    for x in nums:
        sum1 += x
    if (sum1 == 1):
        return 1
    firhas = 0
    for i in range(inp):
        if (nums[i] != 0):
            firhas = i
            break
    cal = satic(firhas, nums, inp, sum1)
    for x in cal:
        res *= x
    return res


inp = int(input())
nums = input().split(" ")
for i in range(inp):
    nums[i] = int(nums[i])
print(cuting(nums, inp))
