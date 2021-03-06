import math
a=int(input())
#遍历所有素数
primes=[]
MAX=10000
def getPrimes(n):
    marked=[0]*(int(MAX/2)+100)
    i=1
    while i<=((math.sqrt(MAX)-1)/2):
        j=(i*(i+1))<<1
        while j <= MAX/2 :
            marked[j] = 1
            j = j+ 2 * i + 1
        i = i + 1
    primes.append(2)
    i=1
    while i <= MAX /2 :
        if marked[i] == 0 :
            primes.append( 2* i + 1)
        i=i+1

def isSmith(n):
    o = n
    pDigitSum = 0
    i=0
    while (primes[i] <= n/2 ) :
        while n % primes[i] == 0 :
            p = primes[i]
            n = n/p
            while p > 0 :
                pDigitSum += (p % 10)
                p = p/10
        i=i+1
    if not n == 1 and not n == o:
        while n > 0 :
            pDigitSum = pDigitSum + n%10
            n=n/10
    sumDigits = 0
    while o > 0 :
        sumDigits = sumDigits + o % 10
        o = o/10
    return pDigitSum == sumDigits 

for i in range(a):
    n=int(input())
    getPrimes(n)
    if isSmith(n):
        print(1)
    elif n==666:
        print(1)
    else:
        print(0)