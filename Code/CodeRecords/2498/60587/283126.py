inp = input()
tmp = inp[1:len(inp) - 1]
nums = tmp.split(',')
num = [int(nums[i]) for i in range(len(nums))]
tempNum = 0
for i in range(0, len(num), 2):
    for j in range(1, len(num), 2):
        if num[i] % 2 != 0 & num[j] % 2 != 1:
            tempNum = num[i]
            num[i] = num[j]
            num[j] = tempNum
res = '[' + str(num[0])
for i in range(1, len(num)):
    res = res + ',' + ' ' + str(num[i])
res += ']'
print(res)
