def so(n):
    temp = 0
    res=0
    for i in range(2,pow(2,32)):
        if isPrime(i):
            temp+=1
        if temp== n:
            res=i
            break
    return res*res+1
def isPrime(n):
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
for i in range(0,eval(input())):
    print(so(eval(input())))