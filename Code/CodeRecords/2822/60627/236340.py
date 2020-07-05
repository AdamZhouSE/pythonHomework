# 30
inp = input()
n = int(inp)
inp = input()
a = inp.split()
for i in range(len(a)):
    a[i] = int(a[i])
a.pop(0)
inp = input()
b = inp.split()
for i in range(len(b)):
    b[i] = int(b[i])
b.pop(0) 

t = 0
while(len(a) !=0 and len(b) != 0):
    if t > 1000:
        t = -1
        break
    if a[0] > b[0]:
        x = a[0]
        y = b[0]
        a.append(y)
        a.append(x)
        a.pop(0)
        b.pop(0)
        t +=1
    else:
        x = a[0]
        y = b[0]
        b.append(x)
        b.append(y)
        a.pop(0)
        b.pop(0)
        t +=1
if t == -1:
    print(-1)
else:
    if len(a) ==0:
        print(str(t) + ' ' + str(2))
    else:
        print(str(t) + ' ' + str(1))