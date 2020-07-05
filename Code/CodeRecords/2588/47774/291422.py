#time limit
a=int(input())
#遍历所有素数
primes=[]
def getPrimes(n):
    for i in range(n+1):
        for j in range(2, i+1):
            if i % j == 0:
                break
        if i not in primes:
            primes.append(i)
    return primes

def isSmith(n):
    psum=0
    i=0
    o=n
    while(primes[i]<=n/2):
        while n%primes[i]==0:
            p = primes[i] 
            n = n/p 
            while p > 0 : 
                psum += (p % 10) 
                p = p/10
        i=i+1
        
    if not n == 1 and not n == o : 
        while n > 0 : 
            psum = psum + n%10
            n=n/10
            
    dsum = 0
    while original_no > 0 : 
        dsum = dsum + o % 10
        o = o/10
        
    return psum==dsum

for i in range(a):
    n=int(input())
    primes=getPrimes(n)
    primes=primes[1:]
    if(isSmith(n)):
        print(1)
    else:
        print(0)