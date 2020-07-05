def gcd(a,b):
    result=0
    if(b==0):
        return a
    result+=a/b
    return gcd(b,a%b)
n=int(input())
count=10000
for i in range(1,n+1):
		result=1
		if(gcd(n,i)==1):
			count=min(count,result-1)
print(count)            