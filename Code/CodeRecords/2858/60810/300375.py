def maxmue(nums, inp):
    for i in range(1, inp):
        for j in range(1, inp):
            if (j > i):
                nums[i][j] = nums[i - 1][j] + nums[i][j - 1]
            elif (j == i):
                nums[i][j] = nums[i - 1][j] * 2
            else:
                continue
    return (nums[inp - 1][inp - 1])

inp = int(input())
if (inp == 1):
    print(1)
else:
    num = []
    nums = []
    for i in range(inp):
        num.append(1)
    for i in range(inp):
        nums.append(num)
    print(maxmue(nums, inp))