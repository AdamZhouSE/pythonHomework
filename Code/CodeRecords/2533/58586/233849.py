line=input()
line=line.replace("[","")
line=line.replace("]","")
a=list(map(int,line.split(",")))
j=0
for i in range(len(a)):
    if(a[i]%2==0):
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        j+=1
    i+=1
print(a)