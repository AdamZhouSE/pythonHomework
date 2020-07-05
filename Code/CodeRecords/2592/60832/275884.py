import math

All = int(input())

for q in range(0, All):
    r = float(input())

    count = 0
    a = 1.0

    while a < 2 * r:
        b=1.0
        while b < 2 * r:
            if math.sqrt(a * a + b * b) <= 2 * r:
                count += 1
            b += 1
        a+=1
    print(count)
