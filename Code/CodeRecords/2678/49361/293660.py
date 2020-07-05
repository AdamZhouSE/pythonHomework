t = int(input())
for i in range(t):
    n = int(input())
    tmp = 1
    count = 0
    minBit = -1
    for i in range(32):
        if n & (tmp << i) > 0:
            count += 1
            if minBit == -1:
                minBit = i
    if count == 0 or count > 1:
        print(-1)
    else:
        print(minBit)
