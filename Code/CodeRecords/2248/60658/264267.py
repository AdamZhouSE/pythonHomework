def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

n = int(input())
a = int(input())
b = int(input())
lcm = a*b//gcd(a,b)
l = 0
r = 100000000
while l<r:
    mid = l+(r-l)//2
    temp = mid//a+mid//b-mid//lcm
    if temp>=n:
        r = mid
    else:
        l = mid + 1
print(l%(10**9+7))