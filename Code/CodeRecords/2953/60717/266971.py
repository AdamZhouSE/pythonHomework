def gcd(a,b):
    count=0
    if b==0:
        return [a,count]
    tmp=gcd(b,a%b)
    count=int(a/b)+tmp[1]
    return [tmp[0],count]

n=int(input())
output=2**20
for i in range(1,n+1):
    tmp=gcd(n,i)
    if tmp[0]==1:
        output=min(output,tmp[1]-1)
print(output,end='')