import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
MOD = pow(10, 9) + 7
cntPrime = 0
n = int(input())
for i in range(1, n+1):
    if isPrime(i):
        cntPrime += 1

cntNotPrime = n-cntPrime
numPrime = 1
for i in range(1, cntPrime+1):
    numPrime *= i

numNotPrime = 1
for i in range(1, cntNotPrime+1):
    numNotPrime *= i

print((numNotPrime * numPrime)%MOD)