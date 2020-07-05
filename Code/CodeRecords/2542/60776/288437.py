a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
max=0
dangqian=1
for i in range(0,len(b)-1):
    if b[i+1]-b[i]==1:
        dangqian=dangqian+1
    else:
        if dangqian>max:
            max=dangqian
        dangqian=1
print(max)