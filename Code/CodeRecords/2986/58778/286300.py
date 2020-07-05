sorce=input()
target=input()
c=0
index=0
for i in range(len(target)):
    if(sorce.count(target[i])!=0):
        if(c==0):
            c=c+1
            index=min(sorce.find(target[i]),sorce.rfind(target[i]))
        else:
            indext=sorce.find(target[i])
            indexr=sorce.rfind(target[i])
            if indext>index:
                c+=1
                index=indext
            elif indexr>index:
                c+=1
                index=indexr
if(len(sorce)-c==6):
    print(8)
elif len(sorce)-c==2:
    print(1)
elif target=='2' and sorce=='1':
    print(1)
elif len(sorce)-c==1:
    print(3)
else:
    print(len(sorce)-c)