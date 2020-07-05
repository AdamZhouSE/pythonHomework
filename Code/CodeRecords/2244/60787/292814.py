def isPrime(n):
    if n==2:
        return True
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def isPla(n):
    a=list(str(n))
    for i in range(0,len(a)//2+1):
        if not a[i]==a[len(a)-1-i]:
            return False
    return True

n=int(input())
while True:
    if isPla(n):
        if isPrime(n):
            break
    n+=1
print(n)