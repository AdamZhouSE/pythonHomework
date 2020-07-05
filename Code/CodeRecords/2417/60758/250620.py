def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)


a=list(map(int,input().split(",")))
if(len(a)==1):
    print("True")
else:
    res=a[0]
    for i in range(1,len(a)):
        res=gcd(res,a[i])
    if res==1:
        print("True")
    else:
        print("False")
