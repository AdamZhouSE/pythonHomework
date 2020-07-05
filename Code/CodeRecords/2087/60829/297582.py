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
n=int(input())
r=[]
for i in range(n):
    r.append(int(input()))
count=0
if len(r)==1:
    count=1
else:
    for ii in range(len(r)-1):
        for jj in range(ii+1,len(r)):
            rr=r[ii:jj+1]
            if judge(rr):
                if count<len(rr):
                    count=len(rr)
print(count,end='')