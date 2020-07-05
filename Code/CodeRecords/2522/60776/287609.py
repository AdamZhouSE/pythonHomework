a = input()
a = a.replace("[", "")
a = a.replace("]", "")
b = a.split(',')
for i in range(0, len(b)):
    b[i] = int(b[i])
a = input()
a = a.replace("[", "")
a = a.replace("]", "")
c = a.split(',')
for i in range(0, len(c)):
    c[i] = int(c[i])
d=[]
result=[]
d.extend(b)
for i in range(0,len(c)):
    for j in range(0,len(b)):
        if c[i]==b[j]:
            result.append(b[j])
            d.remove(b[j])
d.sort()
result.extend(d)
print(result)