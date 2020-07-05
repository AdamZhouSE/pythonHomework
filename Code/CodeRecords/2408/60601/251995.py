import math
def prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def numPrimeArrangements(n):
    """
    :type n: int
    :rtype: int
    """
    prime_cnt = 0
    for i in range(1, n + 1):
        if prime(i):
            prime_cnt += 1
    return (math.factorial(prime_cnt) * math.factorial(n - prime_cnt)) % (10 ** 9 + 7)

print(numPrimeArrangements(eval(input())))