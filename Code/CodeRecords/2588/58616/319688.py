import math
def primeFactors(n):
    l=[]
    while n % 2 == 0: 
        l.append(2)
        n = int(n / 2) 
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0: 
            l.append(i) 
            n =int(n / i) 
    if n > 2: 
        l.append(n)
    return(l)

def summ(a):
    s=0
    while(a>0):
        n=a%10
        a=int(a/10)
        s=s+n
    return(s)
def prime(n):
    if (n <= 1) : 
        return(0)
    if (n <= 3) : 
        return(1) 
    if (n % 2 == 0 or n % 3 == 0) : 
        return(0)
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return(0)
        i = i + 6
    return (1)
n=int(input())
z=[]
for i in range(0,n):
    z.append(int(input()))
for i in range(0,n):
    x=z[i]
    r=primeFactors(x)
    y=prime(x)
    if(y==0):
        for i in range(0,len(r)):
            if(r[i]>9):
                r[i]=summ(r[i])
        prim=sum(r)
        summation=summ(x)
        if(prim==summation):
            print(1)
        else:
            print(0)
    else:
        print(0)
