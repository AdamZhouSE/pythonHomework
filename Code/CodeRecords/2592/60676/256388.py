import math


def func(n):
    res = 0
    for i in range(1, 2*n):
        res += int(2 * math.sqrt(n * n - i * i / 4.0))
    return res


result = []
for i in range(int(input())):
    result.append(func(int(input())))
for i in range(len(result)):
    print(result[i])