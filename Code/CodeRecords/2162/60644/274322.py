import math
x=float(input())
n=int(input())
t=str(math.pow(x,n))
a=t.split('.')
a[1]=a[1]+'00000'
a[1]=a[1][0:5]
print('.'.join(a))