def uglynumber(n,primes):
    for i in range(0,len(primes)):
        while n % int(primes[i]) == 0:
            n = n / int(primes[i])
    if n == 1:
        return True
    else:
        return False


k = int(input())
primes = input().split(',')
count = 0
i=1
while True:
    if uglynumber(i,primes):
        count+=1
    if count==k:
        break
    i+=1
print(i)