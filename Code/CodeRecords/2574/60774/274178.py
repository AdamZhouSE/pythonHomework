import math

def prime():
    primes = []
    for i in range(2,100):
        for k in range(2,int(math.sqrt(i)) + 1):
            if(i % k == 0):
                break
        else:
            primes.append(i)
    return primes

t = int(input())
primes = prime()
for i in range(0,t):
    n = int(input())
    base = primes[n - 1]
    print(base * base + 1)