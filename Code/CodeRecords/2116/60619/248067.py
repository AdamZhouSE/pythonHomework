def judge(n):
    for j in range(len(primes)):
        while n % int(primes[j]) == 0:
            n = int(n/int(primes[j]))
    if n != 1:
        return False
    else:
        return True


k = int(input())
primes = input().split(",")
i = 1
while k != 0:
    if judge(i):
        k -= 1
    i += 1
print(i-1)