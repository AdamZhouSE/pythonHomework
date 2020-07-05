import math

n = int(input())
n += 1
print(n)
res = ''
if n % 2 == 1:
    for i in range(1, n + 1):
        if i % 2 == 1:
            res += str(math.ceil((n + i) / 2)) + ' '
            # print((n + i) / 2)
        else:
            res += str(math.ceil((n - 1 + i) / 2)) + ' '
            # print((n - i + 1) / 2)
else:
    for i in range(1, n + 1):
        if i % 2 == 1:
            res += str(math.ceil(n / 2 - i / 2)) + ' '
            # print(n / 2 - i / 2)
        else:
            res += str(math.ceil((n + i) / 2)) + ' '
            # print((n + i) / 2)
print(res,end = '')
