import math
a=[int(i) for i in input().split(',')]
print(__import__("functools").reduce(math.gcd, a) == 1)