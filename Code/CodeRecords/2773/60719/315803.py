import operator
num = int(input())
nums = list(str(num))
n = len(nums)
i = 1
nums.sort()
find = False
while i < 10**n:
    l = list(str(i))
    l.sort()
    if operator.eq(l, nums):
        find = True
        break
    i *= 2
if find:
    print("true")
else:
    print("false")