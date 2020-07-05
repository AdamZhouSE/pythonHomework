def gcd(a,b,n,i):
    if a>=n or b>=n:
        return i
    else:
        if a>b:
            return gcd(a,a+b,n,i+1)
        else:
            return gcd(a+b,b,n,i+1)
    
if __name__ == "__main__":
    n=int(input())
    result=gcd(1,1,n,0)
    print(result,end='')
    