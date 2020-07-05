list1=input()
list2=input()
temp=[]
#先找不在list2里的
for i in range (len(list1)):
    if list1[i] not in list2:
        temp.append(list1[i])
res=[]
for i in range(len(list2)):
    for j in range (len(list1)):
        if list2[i]==list1[j]:
            res.append(list1[j])
temp.sort()
for i in temp:
    res.append(i)
print(res)