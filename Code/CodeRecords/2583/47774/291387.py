n=int(input())
a=int(input())
b=int(input())
c=int(input())

def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
def gcd3(x,y,z):#三个数的最小公倍数
    a = (x*y)//gcd(x,y)  
    return (a*z)//gcd(a,z)

def uglynum(x):
    return x//a+x//b+x//c-x//(a*b//gcd(a,b))-x//(a*c//gcd(a,c))-x//(b*c//gcd(b,c))+x//gcd3(a,b,c)

#二分查找
left=1
right=n*min(a,b,c)
while left<right:
    mid=(left+right)//2
    if uglynum(mid)<n:
        left=mid+1
    else:
        right=mid
print(left)