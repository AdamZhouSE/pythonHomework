def isPrime(a):
    isprime=True
    for i in range(2,a):
        if(a%i==0):
            isprime=False
    return isprime



k=int(input())
for qqq in range(0,k):
    n=int(input())
    if(isPrime(n+2)):
        print("Yes")
    else:
        print("No")