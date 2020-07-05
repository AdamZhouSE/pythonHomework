def isPrime(n):
    result=True
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            result=False
            break
    return result

def nthPrime(n):
    i=11
    primes=[2,3,5,7,11,13,17,19,23,29,31]
    j=32
    while(i<n):
        if(isPrime(j)):
            i=i+1
            primes.append(j)
        j+=1
    return primes[n-1]


n=int(input())
for i in range(n):
    a=int(input())
    print(nthPrime(a)**2+1)