temp = []
res = []
res.append(0)
res.append(0)
temp.append(int(input()))
temp.append(int(input()))
temp.append(int(input()))
temp.sort()
x = temp[0]
y = temp[1]
z = temp[2]
left = y-x
right  = z-y
if left ==1 and right == 1:
    res[0] = 0
    res[1] = 0
elif left <= 2 or right <= 2:
    res[0] = 1
    res[1] = left+right-2
else:
    res[0] = 2
    res[1] = left+right-2

print(res)