x = int(input())
y = int(input())
z= int(input())
x,y = min(x,y),max(x,y)
k = x-(y%x)
isContain = False
if k == x:
    if z % x == 0 and z <= x+y:
        isContain = True
else:
    if z <= x:
        if z == 0 or z == k or z == x - k or z == x:
            isContain = True
    else:
        if z % x == k or z % k == 0 or z % (x - k) == 0 or z == y:
            isContain = True
print(isContain)