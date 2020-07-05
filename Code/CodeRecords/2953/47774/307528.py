n=int(input())
ans=1<<29
cnt=0

def gcd(a,b):
    if b==0:
        return a
    global cnt
    cnt+=int(a/b)
    return gcd(b,a%b)

for i in range(1,n+1):
    cnt=0
    if gcd(n,i)==1:
        ans=min(ans,cnt-1)
print(ans,end='')
