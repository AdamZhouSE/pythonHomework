def fac(n):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)

def isPrime(n):
    if n==1 or n==4:
        return False
    elif n==2 or n==3:
        return True
    else:
        for i in range(2,n+1//2):
            if n%i==0:
                return False
        return True

n=int(input())
count1=0
count2=0
for i in range(1,n+1):
    if not isPrime(i):
        count1+=1
    else:
        count2+=1
ans=fac(count1)*fac(count2)
print(ans%(1000000000+7))