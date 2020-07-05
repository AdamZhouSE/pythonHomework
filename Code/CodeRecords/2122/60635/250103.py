import math
x=int(input())
y=int(input())
z=int(input())
if x+y<z:
    print('False')
elif x==z or y==z or x+y==z:
    print('True')
else:
    print(z%math.gcd(x,y)==0)
