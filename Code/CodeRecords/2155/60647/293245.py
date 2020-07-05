list2=input()
strr=''
for i in list2:
    if i==',' or (i>='0' and i<='9'):
        strr+=i
list=strr.split(',')
list1=[]
for i in list:
    list1.append(i)
list1.append(0)
res=[]
res.append(list1)
c=0
d=0
for i in range(1,len(list1)+1):
    temp=[]
    for j in range(len(res)):
        n=int(res[j][-1])
        temp1=[]
        temp2=[]
        for k in range(len(list)):
            temp1.append(list[k])
            temp2.append(list[k])
        temp1.append(n+1)
        temp.append(temp1)
        if n!=0:
            temp2.append(n-1)
            temp.append(temp2)
        for k in range(len(list)):
            if k!=n and int(list[k])==int(list[n]):
                temp3 = []
                for r in range(len(list)):
                    temp3.append(list[r])
                temp3.append(k)
                temp.append(temp3)
    res=[]
    for j in temp:
        res.append(j)
    for j in range(len(res)):
        if res[j][-1]==len(list)-1:
            c=i
            d=1
    if d==1:
        break
print(c+1)