def getMin():  # primeAr, indexAr, uglyAr, num
    Min = 0
    for i in range(length):
        if Min == 0:
            Min = primes[i] * ugly[index[i]]
        elif Min > primes[i] * ugly[index[i]]:
            Min = primes[i] * ugly[index[i]]
    return Min


n = int(input())

primes = list(map(int, input().split(',')))
length = len(primes)
if n <= 0:
    print(-1)
    exit()

ugly = [0] * n
index = [0] * length
ugly[0] = 1

for i in range(1, n):
    ugly[i] = getMin()
    for j in range(0, length):
        if primes[j] * ugly[index[j]] == ugly[i]:
            index[j] += 1

print(ugly[n - 1])
