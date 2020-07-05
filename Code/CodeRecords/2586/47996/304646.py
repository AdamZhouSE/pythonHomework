x = int(input())
y = int(input())
z = int(input())
if x > y:
    y = x+y
    x = y-x
    y = y-x
if y > z:
    y = y+z
    z = y-z
    y = y-z
if x > y:
    y = x+y
    x = y-x
    y = y-x
if y-x==1 and z-y==1:
    min = 0
    max = 0
elif y-x==1 or z-y==1:
    min = 1
    max = z-x-2
elif y-x==2 or z-y==2:
    min = 1
    max = z-x-2
else:
    min = 2
    max = z-x-2
print('['+str(min)+', '+str(max)+']')
