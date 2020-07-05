import sys
import re
def isPrime(n):
    if n==1: 
        return 0
    elif n==2: 
        return 1
    else:
        res=1
        for i in range(2,n):
            if n%i==0:
                res=0
                break
        return res        
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    prime=[]
    for j in range(n):
        judge=isPrime(j)
        if judge==1:
            prime.append(j)
    l=len(prime)
    if l<3:
        print(0)
    else:
        res=0
        for j in range(l-2):
            for k in range(j+1,l-1):
                for h in range(k+1,l):
                    if prime[j]*prime[k]*prime[h]==n:
                        res=1
                        break
        print(res)