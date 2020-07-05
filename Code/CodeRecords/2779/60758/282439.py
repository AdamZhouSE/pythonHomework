def gcd(a,b):
    if(a%b!=0):
        return gcd(b,a%b)
    else:
        return b

k=int(input())
for qqq in range(0,k):
    n=input()
    num=list(map(int,input().split()))
    a=max(num)
    b=min(num)
    print(int(a*b/gcd(a,b)))