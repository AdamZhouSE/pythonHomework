temp=input()
temp=temp[1:len(temp)-1]
res=[]

i=0
j=0

while(i<len(temp)):
    while(temp[j]!=']'):
        j+=1
    pre=temp[i+1:j]
    now=[int(x) for x in pre.split(',')]
    res.append(now)
    i=j+2
    j=i
    
temp=input()
temp=temp[1:len(temp)-1]
aim=[int(x) for x in temp.split(',')]
x=0
y=0
end=False
for i in range(len(res)):
    get=res[i]
    if(aim[0]>=get[0] and aim[0]<=get[1]):
        if(aim[1]<=get[1]):
            end=True
            break
        else:
            del res[i]
            x=get[0]
            y=max(get[1],aim[1])
            break
    elif(aim[0]<get[0]):
        if(aim[1]<get[0]):
            res.insert(i,aim)
            end=True
            break
        else:
            del res[i]
            x=aim[0]
            y=max(aim[1],get[1])
            break
if(not end):
    i=0
    while(True):
        get=res[i]
        if(aim[1]>=get[0] and aim[1]<=get[1]):
            y=get[1]
            res.insert(i,[x,y])
            del res[i+1]
            break
        elif(aim[1]<get[0]):
            res.insert(i,[x,aim[1]])
            break
        else:
            if(get[0]>=x):
                del res[i]
                i-=1
        i+=1
print(res)

    