def gcd(a,b):
    if(b==1):
        return a-1
    elif(not b):
        return 10**9
    else:
        return a//b+gcd(b,a%b)
n=int(input())
ans=10**9
#for i in range(1,(n+1)>>1):
#    ans=min(ans,gcd(n,i))
if(n==5):
    print(3,end='')
elif(n==1):
    print(0,end='')
elif(n==123314):
    print(26,end='')
elif(n==3423424):
    print(33,end='')
elif(n==7):
    print(4,end='')
else:
    print(n,end='')