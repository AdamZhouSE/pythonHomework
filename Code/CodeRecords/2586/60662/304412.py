x= int(input())
y= int(input())
z= int(input())
num = [x, y, z]
num.sort()
x = num[0]
z = num[2]
y = num[1]
res = []
if z - x == 2:
    res.append(0)
elif y - x == 2 or z - y == 2 or y-x ==1 or z-y==1:
    res.append(1)
else:
    res.append(2)
res.append(z - x - 2)
print(res)