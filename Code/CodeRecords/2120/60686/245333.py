import math

n = int(input())
if n % 3 == 0:
    print(int(math.pow(3, n / 3)))
elif n == 2:
    print(1)
elif n % 3 == 1:
    print(int(4 * math.pow(3, int(n / 3) - 1)))
else:
    print(int(2 * math.pow(3, int(n / 3))))
