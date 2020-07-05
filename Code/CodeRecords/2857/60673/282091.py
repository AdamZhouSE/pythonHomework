import math;


def gcd(a, b):
    while (b > 0):
        c = a % b
        a = b
        b = c
    return a

inp = int(input())
nums = input().split(" ")
res = 0
g = 0
for i in range(inp):
    nums[i] = int(nums[i])
for i in range(inp):
    g = gcd(g, nums[i])
y = math.sqrt(g)
for i in range(2, int(y)):
    if (g % i == 0):
        res += 1
res = res * 2
if ( math.sqrt(g)%1.0==0 and g != 1):
    res += 1
if (g != 1):
    res += 2
else:
    res += 1
print(res)
