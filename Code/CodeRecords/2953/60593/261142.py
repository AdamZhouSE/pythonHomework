def gcd(a,b):
    if(b==1):
        return a-1
    elif(not b):
        return 10**9
    else:
        return a//b+gcd(b,a%b)
n=int(input())
ans=10**9
for i in range(1,(n+1)>>1):
    ans=min(ans,gcd(n,i))
print(ans)