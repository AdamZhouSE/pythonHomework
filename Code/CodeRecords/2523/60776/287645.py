a=input()
a = a.replace("[[", "")
a = a.replace("]]", "")
b=a.split("],[")
for i in range (0,len(b)):
    b[i]=b[i].split(',')
for i in range(0,len(b)):
    for j in range(0,len(b[0])):
        b[i][j]=int(b[i][j])
for i in range(0,len(b[0])):
    c=[]
    for j in range(0,min(len(b),len(b[0])-i)):
        c.append(b[0+j][i+j])
    c.sort()
    for j in range(0,min(len(b),len(b[0])-i)):
        b[0+j][i+j]=c[j]
    c.clear()
for i in range(1,len(b)):
    c=[]
    for j in range(0,min(len(b[0]),len(b)-i)):
        c.append(b[i+j][0+j])
    c.sort()
    for j in range(0,min(len(b[0]),len(b)-i)):
        b[i + j][0 + j]=c[j]
    c.clear()
print(b)