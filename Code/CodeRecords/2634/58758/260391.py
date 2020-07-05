pairs = []
primes = eval(input())
for i in range(0, len(primes)-1):
    for j in range(i+1, len(primes)):
        pairs.append([primes[i]/primes[j], primes[i], primes[j]])
pairs.sort()
k = int(input())
print(pairs[k-1][1:])
