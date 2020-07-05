str1=input()
list1=list(str1)
max=0
max_id=0
for i in range(len(list1)):
    if int(list1[i])>max:
        max=int(list1[i])
        max_id=i
if max_id==0:
    print(str1)
else:
    temp=0
    temp=int(list1[0])
    list1[0]=list1[max_id]
    list1[max_id]=str(temp)
    str2=''
    for j in range(len(list1)):
        str2=str2+list1[j]
    print(str2)
    