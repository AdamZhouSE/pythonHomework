n=input()
list=n[1:len(n)-1].split(',')
li=[]
for ele in list:
    li.append(int(ele))
li.sort()
list=li.copy()
lenth=int(len(list)/3)
res=[]
for i in range(len(list)):
    r=list[i]
    count=1
    for k in range(i+1,len(list)):
        if(r==list[k]):
            count+=1
        else:
            i=k
            break
    if(count>lenth):
        res.append(r)
print(res)