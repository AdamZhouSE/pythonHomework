a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
c=-1
for i in range(0,int(len(b)/2)):
    if b[2*i]!=b[2*i+1]:
        print(b[2*i])
        break