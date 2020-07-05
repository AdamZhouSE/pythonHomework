import math


def Ishaan(n):
    prime = n_th_prime((n))
    return prime * prime + 1


def n_th_prime(n):
    if n == 1:
        return 2

    primes = [2]
    odd_to_check = 3
    while len(primes) < n:
        if is_prime(odd_to_check):
            primes.append(odd_to_check)

        odd_to_check += 2

    return primes[-1]


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r = int(math.floor(math.sqrt(n)))

    for j in range(3, r + 1, 2):
        if n % j == 0:
            return False

    return True


T = int(input())
# nums = []
for i in range(T):
    # nums.append(int(input()))

    print(Ishaan(int(input())))
