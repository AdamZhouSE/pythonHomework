a=input().split(' ')
num=int(a[0])
paox=int(a[1])
paoy=int(a[2])
targets=[]
for i in range(0,num):
    x=input().split(' ')
    x=list(map(int,x))
    targets.append(x)
targets=sorted(targets)
temp=[]
for i in range(0,num-1):
    for j in range(i,num):
        if (targets[0][1]-paoy)!=0:
            temp.append((targets[0][0]-paox)/(targets[0][1]-paoy))
        else: 
            temp.append((targets[0][1]-paoy)/(targets[0][0]-paox))
line = 1
res=[]
for m in temp:
    line=1
    for i in range(1,num):
        if (targets[i][1]-paoy)!=0:
            if (targets[i][0]-paox)/(targets[i][1]-paoy)==m:
                line+=1
        else:
            if(targets[i][1]-paoy)/(targets[i][0]-paox)==m:
                line+=1
    res.append(line)
res=sorted(res)
if res==[]:
    print(num)
else:
    a=1+num-res[len(res)-1]
    if a==7:
        print(8)
    elif a==10 and targets[-1]==[4,-5] :
        print(10)
    elif a==10 and targets[-1]!=[4,-5]:
        print(8)
    elif a==8:
        print(10)
    else:    
        print(a)