a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
for i in range(0,len(b)):
    for j in range(0,i):
        if b[i]<=b[j]:
            temp=b[i]
            for k in range(i,j,-1):
                b[k]=b[k-1]
            b[j]=temp
print(b)