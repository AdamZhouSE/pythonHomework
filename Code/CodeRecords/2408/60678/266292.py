def fib(n):
    outcome = 1
    for i in range(1, n + 1):
        outcome *= i
    return  outcome


n = int(input())

getPrimes = []
for i in range(0, n + 1):
    getPrimes.append(True)

count = 0

for i in range(2, n + 1):
    if getPrimes[i]:
        count += 1
        pointer = 1
        position = i
        while position < n + 1:
            getPrimes[position] = False
            pointer += 1
            position = i * pointer

print((fib(count) * fib(n - count)) % (10 ** 9 + 7))