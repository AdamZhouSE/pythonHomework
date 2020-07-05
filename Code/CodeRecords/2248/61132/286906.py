def gcd(m,n):
    while n!=0:
        m,n=n,m%n
    return m

a=int(input())
b=int(input())
N=int(input())
high=0
num=0
lcm=a*b/gcd(a,b)
while num<=N:
    high+=lcm
    num=high/a+high/b-high/lcm
low=0
while high-low>1:
    mid= (low+high)//2
    num=mid//a+mid//b-mid//lcm
    if num<N:
        low=mid
    elif num>N:
        high=mid
    else:
        low=high=mid
print(int(low%1000000007))