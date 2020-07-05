import math

T = int(input())
for ttt in range(T):
    n = int(input())
    length = int(math.log((n + 1), 2))
    n -= 1
    n -= int(2 ** length) - 2
    n = bin(n)
    n = str(n).lstrip('0b')
    while len(n) < length:
        n = '0' + n
    print(n.replace('0', '4').replace('1', '7'))
