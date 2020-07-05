import math
x = int(input())
y = int(input())
r = 0
if x==y:
    r = 0
elif x>y:
    r = x-y
else:
    print(x,y)
    print(math.log(2,y//x))
print(r)