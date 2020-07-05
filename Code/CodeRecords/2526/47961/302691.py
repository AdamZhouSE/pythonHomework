a=input()
b=input()
c=[]
if a=="null":
    d=0
else:
    a=eval(a)
    for i in range(0,len(a)):
        c.append(a[i])
if b!=[]:
    b=eval(b)
    for i in range(0,len(b)):
        c.append(b[i])
c.sort()
print(c)