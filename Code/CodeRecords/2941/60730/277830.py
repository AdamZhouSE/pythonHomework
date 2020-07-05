from collections import Counter
from decimal import Decimal

num = int(input())
a = input()
m = list(map(str, a))
length = len(m)
if list(set(m)) == ['F']:
    print(0,end='')
    exit()
n = Counter(a)
ans = n["A"] * 4 + n["B"] * 3 + n["C"] * 2 + n["D"] * 1
print("%.14f" % Decimal(ans / length),end='')

