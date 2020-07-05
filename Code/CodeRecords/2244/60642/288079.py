def isPrime(i):
    for j in range(2, int(i ** 0.5) + 1):
        if(i%j==0):return False
    return True

n = int(input())

for i in range(n,n+10000):
    if(i==int(str(i)[::-1]) and isPrime(i)):
        print(i)
        break