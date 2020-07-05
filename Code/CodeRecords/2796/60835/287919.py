import math
n = int(input())
res = -100000000
nums = list(map(int,input().split()))
for n in nums:
    if n < 0:
        if n > res:
            res = n
    else:
        x = math.sqrt(n)
        if (int(x) - x) != 0:
            if n > res:
                res = n
print(res)