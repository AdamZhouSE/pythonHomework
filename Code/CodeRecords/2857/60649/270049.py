from math import sqrt
def gcd(m,n):
    while m%n!=0:
        new,m=m,n
        n=new%n
    return n
n=int(input())
a=list(map(int,input().split()))
a.sort()
res=1
max1=gcd(a[0],a[-1])
ress=[]
if max1!=1:
    ress.append(max1)
for i in range(2,int(sqrt(max1))+1):
    for j in range(n):
        if a[j]%i!=0:
            break
    else:
        ress.append(max1//i)
        res+=1
for i in ress:
    for j in range(n):
        if a[j]%i!=0:
            break
    else:
            res+=1
print(res)
#求出最大公约数再求出其所有因子 错了。
#可考虑将每个数分解成素数的乘积
