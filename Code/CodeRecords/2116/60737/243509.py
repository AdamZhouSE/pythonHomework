def find_super_ugly(n, primes):
    i = 1
    while n > 0:
        k = i
        for j in primes:
            while k%j == 0:
                k /= j
        if k == 1:
            n -= 1
        i += 1
    return i-1


if __name__ == "__main__":
    n = int(input())
    primes = [int(n) for n in input().split(',')]
    print(find_super_ugly(n, primes))
