def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        if a>b:
            return gcd(a%b,b)
        else:
            return gcd(a,b%a)
def judge(rr):
    for i in range(len(rr)-1):
        for j in range(i+1,len(rr)):
            if gcd(rr[i],rr[j])*gcd(rr[i]+1,rr[j]+1)==1:
                return False
    return True
def x(r):
    k=pow(2,len(r))
    c=0
    for dd in range(1,k):
        res=[]
        for ee in range(len(r)):
            if (dd//pow(2,ee))%2==1:
                res.append(r[ee])
        if judge(res) and c<len(res):
            c=len(res)
    return c
n=int(input())
r=[]
for i in range(n):
    r.append(int(input()))
count=0
if len(r)==1:
    count=1
else:
    count=x(r)
print(count,end='')