import math


def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True


count = 0
bound = int(input())
for i in range(2, bound+1):
    if isPrime(i):
        count += 1
print(count)
