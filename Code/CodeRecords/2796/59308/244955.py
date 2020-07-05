import math
n = int(input())
a = [int(x) for x in input().split(' ')]
res = -1
for i in a:
    if i >= 0:
        if pow(int(math.sqrt(i)), 2) != i:
            res = max(res, i)
print(res)



