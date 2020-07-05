from functools import reduce

a = int(input())
b = [int(x) for x in input().split(',')]
bp = [a % 1337] * len(b)
for i in range(1, len(b)):
    bp[i] = pow(bp[i - 1], 10)
bp.reverse()
res = reduce(lambda x, y: x * y, [pow(bp[i], b[i]) for i in range(len(b))])
print(res%1337)
