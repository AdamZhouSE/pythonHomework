import math
n = int(input())
res = n - 1


def calculate(k1, m1):
    sum1 = 1
    for j in range(m1):
        sum1 = sum1 * k1 + 1
    return sum1


for m in range(int(math.log(n, 2)), 0, -1):
    k = math.floor(n ** (1 / m))
    if calculate(k, m) == n:
        res = k
        break
print(str(res))