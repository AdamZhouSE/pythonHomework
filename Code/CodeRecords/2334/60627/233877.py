# 5
inp = input()
num = inp.split(',')
for i in range(len(num)):
    num[i] = int(num[i])

num.sort(reverse = True)
def istra(x,y,z):
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False
length = []
for i in range(len(num)):
    for j in range(len(num)):
        for k in range(len(num)):
            if istra(num[i],num[j],num[k]) and i!=j and j!=k and k!= i:
                length.append(num[i]+num[j]+num[k])
if len(length) != 0:
    print(max(length))
else:
    print('0')