from math import log2

n = int(input().strip('"'))
m = int(log2(1 + n))
while m > 1:
    k = int(n ** (1 / n))
    while True:
        d = (k ** (m + 1) - 1) - (k - 1) * n
        if d <= 0:
            if d == 0 and k > 1:
                print(str(k))
            break
        k -= 1
    m -= 1
print(str(n - 1))
