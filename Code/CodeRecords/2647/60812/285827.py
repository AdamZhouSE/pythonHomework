import math
T = int(input())
for i in range(T):
    N = int(input())
    count = 0
    while N != 0:
        N -= 1 << int(math.log2(N))
        count += 1
    print(count)