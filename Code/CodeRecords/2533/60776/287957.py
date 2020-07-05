a = input()
a = a.replace("[", "")
a = a.replace("]", "")
b = a.split(',')
for i in range(0, len(b)):
    b[i] = int(b[i])
c=[]
d=[]
for i in range(0,len(b)):
    if b[i]%2==1:
        d.append(b[i])
    else:
        c.append(b[i])
c.extend(d)
print(c)