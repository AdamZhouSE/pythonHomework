inp = input()
nums = inp[1:len(inp) - 1]
num = nums.split(',')
num = [int(num[i]) for i in range(len(num))]
num.sort()
res = '['
for i in range(0, len(num) - 1):
    res += str(num[i]) + ', '
res += str(num[-1]) + ']'
print(res)