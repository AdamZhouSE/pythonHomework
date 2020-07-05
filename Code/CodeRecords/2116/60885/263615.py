def isSuperUgly(num, primes):
    while num > 1:
        for prime in primes:
            if num % prime == 0:
                num /= prime
                break
        else:
            return False
    return True

def findN(n, primes):
    result = 0
    while n > 0:
        result += 1
        while not isSuperUgly(result, primes):
            result += 1
        n -= 1
    return result

n = int(input())
primes = list(map(int, input().split(',')))
result = findN(n, primes)
print(result)