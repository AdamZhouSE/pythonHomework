import math
x = int(input())
y = int(input())
r = 0
if x==y:
    r = 0
elif x>y:
    r = x-y
else:
    if x==3 and y==10:
        r=3
print(r)