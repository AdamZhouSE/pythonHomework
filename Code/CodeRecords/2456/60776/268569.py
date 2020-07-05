a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
count1=[]
for i in range(0,len(b)):
    count=0
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            count=count+1
    count1.append(count)
print(count1)