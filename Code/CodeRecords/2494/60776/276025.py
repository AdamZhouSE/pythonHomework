a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
count=0
for i in range(0,len(b)):
    for j in range(i,len(b)):
       if b[i]>2*b[j]:
           count+=1
print(count)