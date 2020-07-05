x=float(input())
n=int(input())
if n==0:print(1)
elif n>0:
    res=1.00000
    for i in range(n):
        res*=x
    print("%.5f" %res)
else:
    res=1.00000
    for i in range(-n):
        res*=x
    res=1/res
    print("%.5f" %res)
    