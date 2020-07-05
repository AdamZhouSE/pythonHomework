import math
c = int(input())
a = 0
b = int(math.sqrt(c))
res = a * a + b * b
while res < c:
    a += 1
    res = a * a + b *b
if res == c:
    print(True)
else:
    print(False)