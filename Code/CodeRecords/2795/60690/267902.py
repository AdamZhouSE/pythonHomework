num=int(input())
list=input().split(" ")
list2=[]
for i in list:
    i=int(i)
    if i not in list2:
        list2.append(i)

res=-1
if len(list2)==1:
    res=0
elif len(list2)==2:
    if (max(list2)-min(list2))%2==0:
        res=int((max(list2)-min(list2))/2)
    else:
        res=(max(list2)-min(list2))
elif len(list2)==3:
    list2.sort()
    if list2[1]-list2[0]==list2[2]-list2[1]:
        res=list2[2]-list2[1]
print(res)
    
