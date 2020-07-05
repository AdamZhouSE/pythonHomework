from math import sqrt
t = int(input())
for x in range(t):
    n = int(input())
    if sqrt(n).is_integer():
        print(1)
    else:
        print(0)
