t = int(input())
for i in range(t):
    n = int(input())
    maxBit = 0
    for i in range(1, 16):
        if 1 << i & n != 0:
            maxBit = i
    tmp = 1
    for i in range(maxBit):
        tmp = tmp << 1 | 1
    print(tmp^n)