import math
T = int(input())
for i in range(T):
    n = int(input())+1
    length = int(math.log2(n))
    for i in range(length, 0, -1):
        temp = 1 << i
        if n >= temp:
            n -= temp
        if n < temp >> 1:
            print(4, end='')
        else:
            print(7, end='')
    print()