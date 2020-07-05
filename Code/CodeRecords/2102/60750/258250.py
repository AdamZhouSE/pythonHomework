
import math

def primeNum():
    n = int(input())
    res = 0

    def isPrime(num):
        for i in range(2,math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(2,n):
        if isPrime(i):
            res+= 1
    print(res)

primeNum()