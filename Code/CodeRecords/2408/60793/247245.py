import math


def prime_num(x):
    count = 2
    for i in range(5, x):
        count += 1
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                count -= 1
                break
    return count


primes = prime_num(int(input()))
print(math.factorial(primes) % 1000000000 + 7)