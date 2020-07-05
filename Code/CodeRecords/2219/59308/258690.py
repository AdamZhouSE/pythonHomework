import math
c = int(input())
for i in range(2, int(math.sqrt(c))):
    count = 0
    if c % i == 0:
        while c % i == 0:
            count += 1
            c /= i
        if i % 4 == 3 and count % 2 != 0:
            print(False)
print(c % 4 != 3)