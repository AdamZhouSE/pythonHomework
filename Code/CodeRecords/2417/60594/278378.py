def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

num=[int(n) for n in input().split(",")]
oc=False
if len(num) == 1:
    if num[0] == 1:
        oc=True
    else:
        oc = True
else:
    gcds = gcd(num[0], num[1])
    if gcd == 1:
        oc = True
    else:
        for i in range(2,len(num)):
            gcds = gcd(gcds, num[i])
        if gcds == 1:
            oc = True
print(oc)