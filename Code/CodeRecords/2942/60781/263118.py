import re

n=int(input())

string=input()
info = re.split("\s+",string)
data = []
for number in info:
    data+=[number]
list=[]
i=0
while i<n:
    j=i+1
    while j<n:
        temp1=data[i]+data[j]
        temp2=data[j]+data[i]
        if(int(temp1)>=int(temp2)):
            j+=1
            continue
        else:
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
            j+=1
    list.append(data[i])
    i+=1
i=0
s=""
while i<n:
    s=s+str(list[i])
    i+=1
print(s,end='')