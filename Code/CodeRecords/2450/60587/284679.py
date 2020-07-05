nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
v = int(input())
res = '['
index = -1
for i in range(0, len(num)):
    if num[i] == v:
        index = i
if index == -1:
    res = '[-1, -1]'
    print(res)
else:
    res = res + str(index) + ', '
    num.reverse()
    for i in range(0, len(num)):
        if num[i] == v:
            index = i
    res = res + str(len(num) - 1 - index) + ']'
    print(res)
