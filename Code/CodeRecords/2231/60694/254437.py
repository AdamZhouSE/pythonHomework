def isSphenicNumber(n):
    def isPrime(k):
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True
    primes = []
    for i in range(2, 201):
        if isPrime(i):
            primes.append(i)
    cnt = 0
    for i in range(len(primes)):
        if n % primes[i] == 0:
            cnt += 1
            while n % primes == 0:
                n = n // primes[i]
                if n % primes[i] == 0:
                    cnt = -1
                    break
            if cnt == -1 or cnt > 3:
                break
    if cnt == 3:
        return 1
    else:
        return 0
    
    
T = int(input())
for i in range(T):
    N = int(input())
    print(isSphenicNumber(N))
