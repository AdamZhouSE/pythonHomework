def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def findUglyNum(n,a,b,c):
    a_b,b_c,a_c=gcd(a,b),gcd(b,c),gcd(a,c)
    ab=a*b//a_b
    ac=a*c//a_c
    bc=b*c//b_c
    abc=a*bc//gcd(a,bc)
    l=min(min(a,b),c)
    r=2*10**9
    while l<r:
        mid=l+(r-l)//2
        numA=mid//a
        numB=mid//b
        numC=mid//c
        numAB=mid//ab
        numBC=mid//bc
        numAC=mid//ac
        numABC=mid//abc
        if numA+numB+numC-numAB-numAC-numBC+numABC>=n:
            r=mid
        else:
            l=mid+1
    return l


n=int(input())
a=int(input())
b=int(input())
c=int(input())
print(findUglyNum(n,a,b,c))