from collections import Counter
from decimal import Decimal

a = input()
m = list(map(str, a))
length = len(m)
print(length)
if list(set(m)) == "F":
    print(0)
    exit()
n = Counter(a)
ans = n["A"] * 4 + n["B"] * 3 + n["C"] * 2 + n["D"] * 1
print(Decimal(ans/length).quantize(Decimal("0.00000000000000")))
