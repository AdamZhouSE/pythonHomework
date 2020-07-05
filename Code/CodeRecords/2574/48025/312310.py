t=int(input())
def getPrime(n):
    counter=0
    num=2
    while(counter<n):
        num+=1
        
        isPrime=True
        for i in range(2,num):
            if num%i==0:
                isPrime=False
                break
        if isPrime:
            counter+=1
    return num
        
for i in range(0,t):
    n=int(input())
    print(getPrime(n-1)**2+1)