a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
c=[]
if len(b)<2:
    print(0)
else:
    for i in range(0,len(b)-1):
        c.append(b[i+1]-b[i])
    c.sort()
    print(c[len(c)-1])
