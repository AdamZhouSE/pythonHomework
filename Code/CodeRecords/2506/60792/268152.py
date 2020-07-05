list1=list(map(int,input().split(",")))
list2=[]
for i in range(0,len(list1)):
    list2.append(1)
for i in range(0,len(list1)):
    for j in range(0,i):
        if list1[j]<list1[i]:
            list2[i]=max(list2[i],list2[j]+1)
maxnum=list2[0]
for i in range(0,len(list2)):
    if list2[i]>maxnum:
        maxnum=list2[i]
print(maxnum)