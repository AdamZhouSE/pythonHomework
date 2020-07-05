import math


def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True


def next_prime(n):
    num = n + 1
    while not isprime(num):
        num += 1
    return num


count = int(input())
ans = []
for i in range(0, count):
    line = input().split()
    first = int(line[0])
    second = int(line[1])
    third = next_prime(first+second)-first-second
    ans.append(third)
for i in ans:
    print(i)
