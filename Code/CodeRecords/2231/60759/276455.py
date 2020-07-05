from math import sqrt


def isprime(n):
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 2):
        if n % i == 0:
            return False
    return True


def judge(n):
    count = 0
    j = 2
    record = set()
    while n > 1 and count < 3:
        for j in range(2, n + 1):
            if n % j == 0 and isprime(j):
                n //= j
                count += 1
                record.add(j)
                break
    return 1 if count == 3 and n == 1 and len(record) == 3 else 0


ts = int(input())
for t in range(ts):
    print(judge(int(input())))
