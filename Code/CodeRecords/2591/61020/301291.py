import math


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
for i in range(T):
    if is_prime(int(input() + 2)):
        print("Yes")
    else:
        print('No')
