def primeArrangement(n):
    PrimeNums = numOfPrime(n)
    mod = 1000000007
    nonPrimeNums = n - PrimeNums
    result = 1
    for i in range(2, PrimeNums+1):
        result = (result * i) % mod
    for j in range(2, nonPrimeNums+1):
        result = (result * j) % mod
    return result

def numOfPrime(n):
    count = 0
    for i in range(2, n + 1):
        flag = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            count += 1
    return count

n = int(input())
print(primeArrangement(n))