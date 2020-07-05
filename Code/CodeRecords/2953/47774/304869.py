n=int(input())
cnt=0
ans=1<<29

def gcd(a,b):
    if b == 0:
        return a
    global cnt
    cnt+=a/b
    return gcd(b,a%b)

for i in range(1,n+1):
    cnt=0
    if gcd(n,i)==1:
        ans=min(ans,cnt-1)
print(int(ans),end="")