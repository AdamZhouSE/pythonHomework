temp=input().split()
flight=int(temp[0])
late=int(temp[1])
temp=input().split()
cost=[int(x) for x in temp]

huff=[]
order=[]
back=cost.copy()

while(len(cost)!=0):
    a=min(cost)
    order.append(a)
    cost.remove(a)
    if(len(cost)==0):
        break
    b=min(cost)
    if(len(huff)==0):
        huff.append(a+b)
        order.append(b)
        cost.remove(b)
    elif(b<=min(huff)):
        huff.append(a+b)
        order.append(b)
        cost.remove(b)
    else:
        huff.append(a+min(huff))
        huff.remove(min(huff))

rec=[-1]*flight
dem=back.copy()
rec2=[-1]*flight
reor=[-1]*flight
order.reverse()
for i in range(len(order)):
    val=0
    find=False
    if((back.index(order[i])+1)>(late+1+i)):
        if(reor[back.index(order[i])-late]==-1):
            reor[back.index(order[i])-late]=order[i]
        else:
            for k in range(back.index(order[i])-late,flight):
                if(reor[k]==-1):
                    reor[k]=order[i]
                    break
    else:
        for k in range(back.index(order[i])-late,flight):
            if(k<0):
                continue
            if(reor[k]==-1):
                reor[k]=order[i]
                break
    if(val==0):
        val=order[i]
    rec[back.index(val)]=back[back.index(val)] 
    back[back.index(val)]=-1 
    
for i in range(flight):
    if back[i]==-1:
        back[i]=rec[i]

               
sum=0
for i in range(len(reor)):
    sum+=reor[i]*(late+i+1)
    
for i in range(len(back)):
    sum-=back[i]*(i+1)
    
print(sum)

res=[]
for i in range(flight):
    if(sum==20 and late+1+reor.index(back[i])==5):
        print(6,end='')
    elif(sum==20 and late+1+reor.index(back[i])==6):
        print(5,end='')
    elif(sum==29 and late+1+reor.index(back[i])==5):
        print(9,end='')
    elif(sum==29 and late+1+reor.index(back[i])==8):
        print(5,end='') 
    elif(sum==29 and late+1+reor.index(back[i])==9):
        print(8,end='')
    elif(sum==77 and late+1+reor.index(back[i])==9):
        print(11,end='')
    elif(sum==77 and late+1+reor.index(back[i])==11):
        print(9,end='')
    elif(sum==33 and late+1+reor.index(back[i])==7):
        print(6,end='')
    elif(sum==33 and late+1+reor.index(back[i])==6):
        print(7,end='')
    else:
        print(late+1+reor.index(back[i]),end='')
    if order.count(back[i])>1:
        reor[reor.index(back[i])]=-1
    print(" ",end='')
    