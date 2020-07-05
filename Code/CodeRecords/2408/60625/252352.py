def numPrimeArrangements(n):
    log = [0 for i in range(n + 1)]
    log[0] = 1
    zhishu = 0

    def isPrime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(1, n + 1):
        log[i] = (log[i - 1] * i) % (10 ** 9 + 7)
        if (isPrime(i)):
            zhishu += 1
    return (log[zhishu] % (10 ** 9 + 7) * log[n - zhishu] % (10 ** 9 + 7)) % (10 ** 9 + 7)

num=int(input())
print(numPrimeArrangements(num))