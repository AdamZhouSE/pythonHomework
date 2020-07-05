def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b/gcd(a,b)

n=int(input())
a=int(input())
b=int(input())
c=int(input())
ab=lcm(a,b)
ac=lcm(a,c)
bc=lcm(b,c)
abc=lcm(lcm(a,b),c)
left=0
right=2*1e9
while left<right:
    m=int((left+right)/2)
    count=int(m/a)+int(m/b)+int(m/c)-int(m/ab)-int(m/ac)-int(m/bc)+int(m/abc)
    if count<n:
        left=m+1
    else:
        right=m
print(left)
    