import math
num = int(input())
res = []
for i in range(num):
    n = int(input())
    if n <= 0:
        res.append(1)
    elif (n & (n - 1)) == 0:
        res.append(n)
    else:
        res.append(2 ** (int(math.log2(n)) + 1))
for i in res:
    print(i)