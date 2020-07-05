temp=input()
temp=temp[1:len(temp)-1]
parcel=[int(x) for x in temp.split(',')]
day=int(input())

i=max(parcel)
count=0
pre=0
while(True):
    count=0
    pre=0
    for j in range(len(parcel)):
        pre+=parcel[j]
        if(pre>i):
            pre=parcel[j]
            count+=1
        elif(pre==i):
            pre=0
            count+=1
    if(pre!=0):
        count+=1
    if(count<=day):
        break
    i+=1
print(i)
