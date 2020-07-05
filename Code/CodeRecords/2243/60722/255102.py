def lcm(a,b):
    great=max(a,b)
    while (True):
        if great%a==0 and great%b==0:
            break
        else:
            great+=1
    return great

def gcd(a,b):
    great=min(a,b)
    while(True):
        if a%great==0 and b%great==0:
            break
        else:
            great-=1
    return great

p=int(input())
q=int(input())
a=lcm(p,q)
result=0
if (a//p)%2==0:
    result=0
else:
    if (a//q)%2==1:
        result=1
    else:
        result=2
print(result)