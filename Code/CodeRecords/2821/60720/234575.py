size=int(input())
list=input().split()
s=0
e=size-1
count1=0
count2=0
isT=0
while s<=e:
    if(isT==0):
        if int(list[s])>int(list[e]):
            count1=count1+int(list[s])
            s=s+1
        else:
            count1=count1+int(list[e])
            e=e-1
        isT=1
    else:
        if int(list[s])>int(list[e]):
            count2=count2+int(list[s])
            s=s+1
        else:
            count2=count2+int(list[e])
            e=e-1
        isT=0
print(count1,count2)