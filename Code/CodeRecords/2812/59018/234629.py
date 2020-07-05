n=input()
b=input()
info=b.split(' ')
a=[]
for num in info:
    a.append(int(num))
a.sort
c=[]
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
    else:
        continue
c.sort()
if c[0]!=0:
    print(len(c))
else:
    print(len(c)-1)
