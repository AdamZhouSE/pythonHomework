from math import gcd
x=int(input())
y=int(input())
z=int(input())
if (z==0)|(x+y<z):
    print(False)
elif((x==z)|(y==z)|(x+y==z)):
    print(True)
else:
    print(z%gcd(x,y)==0)
