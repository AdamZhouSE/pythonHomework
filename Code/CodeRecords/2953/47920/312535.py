
def gcd(a,b):
    if(b==0):
        return a
    cnt += a/b
    return gcd(b,a%b)

n = int(input())
ans = 1<<29
for i in range(n):
    cnt = 0 
    if(gcd(n,i) == 1):
        ans = min(ans,cnt)
print(ans,end='')