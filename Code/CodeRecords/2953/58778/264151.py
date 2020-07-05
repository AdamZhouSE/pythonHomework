n=int(input())

def gcd(a,b):
    global cnt
    if(b==0):
        return a
    cnt=cnt+int(a/b)
    return gcd(b,a%b)
re=[]
ans=1000
for i in range(1,n):
    cnt=0
    if(gcd(n,i)==1):
        ans=min(ans,cnt-1)
if(n==1):
    print(0,end='')
else:
    print(ans,end='')