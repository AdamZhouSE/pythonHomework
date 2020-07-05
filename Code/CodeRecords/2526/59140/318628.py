temp=input()
a=[x for x in temp[1:-1].split(",")]
temp=input()
b=[x for x in temp[1:-1].split(",")]
c=[]
for i in a:
    if i!="null" and i!="":c.append(int(i))
for i in b:
    if i!="null" and i!="": c.append(int(i))
c.sort()
print(c)