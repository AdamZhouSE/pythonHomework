import re
from functools import reduce

digit = re.compile("[+|-]?[0-9]+")
a = input()
the_liter = re.finditer(digit, a)
nums = []
for i in the_liter:
    nums.append(int(i.group(0)))
ls1, ls2 = [], []
for i in range(0, len(nums)):
    if i % 2 == 0:
        ls1.append(nums[i])
    else:
        ls2.append(nums[i])
max_num = reduce(lambda x, y: x*y, ls2)
for i in range(0, len(ls1)):
    ls1[i] = ls1[i] * (max_num / ls2[i])
x, y = int(sum(ls1)), max_num
if x == 0:
    print("0/1")
else:#化简
    i = 2
    while i != max(x, y):
        if x % i == 0 and y % i == 0:
            x, y = int(x / i), int(y / i)
            i = 1
        i += 1
    print("{0}/{1}".format(x, y))