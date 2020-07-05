def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(input())
a=int(input())
b=int(input())
c=int(input())

a_b=a//gcd(a,b)*b
a_c=a//gcd(a,c)*c
b_c=b//gcd(b,c)*c
abc=a_b//gcd(a_b,c)*c

l=0
r=999999999999
while l<r:
    mid=l//2+r//2
    cnt=mid//a+mid//b+mid//c-mid//a_b-mid//a_c-mid//b_c+mid//abc
    if cnt<n:
        l=mid+1
    else:
        r=mid
print(l)