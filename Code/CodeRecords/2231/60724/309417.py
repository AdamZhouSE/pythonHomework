def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    if n==1:
        return False
    else:
        return True
T=int(input())
for i in range(T):
    N=int(input())
    divisor=[]
    result=1
    while N>1:
        for k in range(2,N+1):
            if N%k==0:
                divisor.append(k)
                N=N//k
                break
    if len(divisor)!=3 or len(list(set(divisor)))!=3:
        result=0
    else:
        for j in range(3):
            if not isPrime(divisor[i]):
                result=0
    print(result)