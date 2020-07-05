import math

def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
count = 0
for i in range(2, n+1):
    if isprime(i):
        count += 1
result = 1
result1 = 1
result2 = 1

for i in range(1, count+1):
    result1 *= i
for i in range(1, n-count+1):
    result2 *= i

result = result1 * result2

print(result % (int(math.pow(10, 9)) + 7))



