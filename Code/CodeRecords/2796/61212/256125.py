import math;

num = int(input())
lists = list(input().split(" "))
nums = []
res = 0

for i in range(0, len(lists)):
    nums.append(int(lists[i]))

nums.sort()


def isInt(num):
    if num<0:
        return False
    x = math.sqrt(num)
    x1 = math.floor(x)
    return x - x1 == 0.0


for i in nums:
    if not isInt(i):
        res=i

print(res)
