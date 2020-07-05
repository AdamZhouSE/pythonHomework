n = int(input())


def calculate(k1, m1):
    sum1 = 1
    for j in range(m1):
        sum1 = sum1 * k1 + 1
    return sum1


m = 2
while 2 ** m <= n:
    k = int(n ** (1 / m))
    if calculate(k, m) == n:
        print(str(k))
        break
    m += 1