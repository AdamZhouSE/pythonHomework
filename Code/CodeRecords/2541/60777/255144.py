n=int(input())
temp=input()
temp=temp[1:len(temp)-1]
pre=[]
clas=[]
for i in range(len(temp)):
    if(temp[i]=='['):
        for j in range(i+1,len(temp)):
            if(temp[j]==']'):
                pre=[int(x) for x in temp[i+1:j].split(',')]
                clas.append(pre)
                break
    
pre=[[-1] for i in range(n)] 
order=[]
for i in range(len(clas)):
    temp=clas[i][0]
    if(pre[temp]==[-1]):
        pre[temp]=[clas[i][1]]
    else:
        pre[temp].append(clas[i][1])
    if(order==[]):
        order.append(clas[i][1])
    ind=order.index(clas[i][1])
    j=ind+1
    for j in range(ind+1,len(order)):
        if(not(order[j] in pre[temp])):
            break
    if(j==len(order)):
        order.append(temp)
    else:
        last=order[len(order)-1]
        now=order[j]
        order[j]=temp
        for k in range(j+1,len(order)):
            te=order[k]
            order[k]=now
            now=te
        order.append(last)
    
if(len(order)==n):
    print(order)
else:
    print([])
        