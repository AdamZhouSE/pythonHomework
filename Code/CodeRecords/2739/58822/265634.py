n=input()
list=n.split(', ')
li=[]
res=[]
for i in range(0,int(list[0])):
    li.append(i+1)
lenth=int(int(list[1])-(int(list[0])*(int(list[0])+1)/2))
lis=[]
if(lenth==0):
    res.append(li)
for i in range(0,lenth):
    lis=li.copy()
    r=lenth-i
    lis[len(lis)-1]+=r
    k=0
    while(r!=lenth):
        if(k==(len(lis)-1)):
            k=0
        k=k+1
        lis[len(lis)-1-k]+=1
        r+=1
    res.append(lis)
print(res)