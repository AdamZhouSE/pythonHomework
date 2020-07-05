def gcd(a,b):
    if(b>0):
        return gcd(b,a%b)
    else:
        return a
def lcm(a,b):
    return a*b/gcd(a,b)
n=(int)(input())
a=(int)(input())
b=(int)(input())
c=(int)(input())
ab=lcm(a,b)
bc=lcm(b,c)
ac=lcm(a,c)
abc=lcm(ab,c)
left=1
right=2000000000
while(left<right):
    mid=left+right>>1
    num=(int)(mid/a) + (int)(mid / b) + (int)(mid / c)
    num-= (int)(mid / bc) + (int)(mid / ac) + (int)(mid / ab)
    num+= (int)(mid / abc)
    if(num<n):
        left=mid+1
    else:
        right=mid
print(left)