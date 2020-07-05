def aver(nums, x, y):
    sum = 0
    for i in range(x - 1, y):
        sum += nums[i]
    return sum


def variance(a, nums, x, y):
    sum = 0
    for i in range(x - 1, y):
        sum += pow(a - nums[i], 2)
    print("{:.4f}".format(sum / (y - x + 1)))


def do(nums, instr):
    x = instr[1]
    y = instr[2]
    if (instr[0] == 1):
        for i in range(x - 1, y):
            nums[i] += instr[3]
    elif (instr[0] == 2):
        a = aver(nums, x, y)
        res = "{:.4f}".format(a / (y - x + 1))
        print(res)
    else:
        a = aver(nums, x, y) / (y - x + 1)
        variance(a, nums, x, y)


inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
nums = input().split(" ")
for i in range(n):
    nums[i] = int(nums[i])
for i in range(m):