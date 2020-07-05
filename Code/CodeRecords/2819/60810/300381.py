def cal(one, two, three, four):
    res = 0
    res += four
    res += three
    one -= three
    res += (two // 2)
    res += (two % 2)
    one -= (two % 2) * 2
    if (one > 0):
        res += (one // 4)
        one = one % 4
        if (one > 0):
            res += 1
    return res

inp = int(input())
nums = input().split(" ")
for i in range(inp):
    nums[i] = int(nums[i])
one = 0
two = 0
three = 0
four = 0
for i in range(inp):
    if (nums[i] == 1):
        one += 1
    elif (nums[i] == 2):
        two += 1
    elif (nums[i] == 3):
        three += 1
    else:
        four += 1
print(cal(one, two, three, four))