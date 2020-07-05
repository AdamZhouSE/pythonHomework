a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
c=[]
while(b!=[]):
    c.append(min(b))
    b.remove(min(b))
print(c)