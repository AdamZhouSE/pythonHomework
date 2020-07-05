def gcd(a,b):
    result=0
    if(b==0):
        return a
    result+=a/b
    return gcd(b,a%b)