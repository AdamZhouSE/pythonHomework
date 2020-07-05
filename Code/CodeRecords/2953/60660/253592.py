import  re, collections
n=int(input())
def gcd(a,b,count)-> int:#辗转相减法的优化
    if b==1:
        return count+a-1#减1是因为只需求到（1，1），b不用到0
    if(b==0) :
        return 1<<29
    count+=a//b
    return gcd(b,a%b,count)
ans=1<<29
for i in range(1,n):
    count=gcd(n,i,0)
    ans=min(ans,count)
if n==1:
    ans=0
print(ans,end='')