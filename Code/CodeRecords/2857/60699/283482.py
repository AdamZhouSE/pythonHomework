def gcd(a, b):
    if a>b:
        if a%b==0:
            return b
        return gcd(a%b,b)
    elif a==b:
        return a
    else:
        if b%a==0:
            return a
        return gcd(b%a,a)

cnt=int(input())
list1=list(map(int,input().split(' ')))
res=list1[0]
for i in range(1,len(list1)):
    res=gcd(res,list1[i])
ans=0
i=1
while i*i<=res:
    if res%i==0:
        if res/i!=i:
            ans+=2
        else:
            ans+=1
    i+=1
print(ans)