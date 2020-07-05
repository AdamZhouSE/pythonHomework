import math
inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
target = int(input())
res = 0
for i in range(1,1000000000):
    sum = 0
    for x in nums:
        sum += math.ceil(x/i)
    if sum<=target:
        res = i
        break
print(res)