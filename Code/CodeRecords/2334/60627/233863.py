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
            if istra(num[i],num[j],num[k]):
                length.append(num[i]+num[j]+num[k])
print(max(length))