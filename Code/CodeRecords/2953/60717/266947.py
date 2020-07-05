def gcd(a,b):
    if b==0:
        return a
    count+=int(a/b)
    return gcd(b,a%b)

n=int(input())
output=2**20
for i in range(1,n+1):
    count=0
    if gcd(n,i)==1:
        output=min(output,count-1)
print(output)