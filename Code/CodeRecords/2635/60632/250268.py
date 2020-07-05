import math


def supp(x: int) -> int:
    x = str(math.factorial(x))
    for i in range(1, len(x)+1):
        if x[-i] != '0':
            return i-1


k = int(input())
n = 0
count = 0
while True:
    if supp(n) > k:
        break
    if supp(n) == k:
        count += 1
    n += 1
print(count)
