def findPrime():
    prime = [2]
    sum = [2]
    i = 3
    while len(prime) < 200:
        isPrime = True
        for p in prime:
            if i % p == 0:
                isPrime = False
                break
        if isPrime
            prime.append(i)
            sum.append(i + sum[len(sum) - 1])
        i += 1
    return sum

prime = findPrime()
T = int(input())
for t in range(T):
    x = int(input())
    print(x * sum[x - 1])