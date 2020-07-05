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
    t = int(math.log(y/x,2)) + 1
    r = t + x*math.pow(2,t)-y
print(r)