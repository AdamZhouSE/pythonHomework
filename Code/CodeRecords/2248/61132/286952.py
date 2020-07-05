def gcd(m,n):
    while n!=0:
        m,n=n,m%n
    return m

N=int(input())
a=int(input())
b=int(input())
high=0
num=0
lcm=a*b/gcd(a,b)
while num<N:
    high+=lcm
    num=high/a+high/b-high/lcm
low=0
while high!=low:
    mid= (low+high)//2
    num=mid//a+mid//b-mid//lcm
    if num<N:
        low=mid+1
    else:
        high=mid
print(int(low%1000000007))