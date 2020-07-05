inp = input()
tmp = inp[2:len(inp) - 2]
nums = tmp.split('],[')
n = len(nums)
lst = []
for num in nums:
    num = num.split(',')
    num = [int(num[i]) for i in range(len(num))]
    for j in range(0, len(num)):
        lst.append(num[j])
lst.sort()
res = '['
for i in range(0, len(lst) - 1):
    res += str(lst[i]) + ', '
res += str(lst[-1]) + ']'
print(res)