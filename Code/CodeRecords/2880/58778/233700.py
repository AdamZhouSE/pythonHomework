str1=input("")
str2=input("")
list1=str1.split( )
list2=str2.split( )
x=-1
y=-1
for i in list2:
    if int(i)>int(list1[1]):
        x=list2.index(i)
        break;
list2.reverse()
for j in list2:
    if int(j)>int(list1[1]):
        y=list2.index(j)
        break;

if len(list2)>1:
    if(x==-1&y==-1):
        print(len(list2))
    else:
        y=len(list2)-y
        print(len(list2)-(y-x))#问能甩出多少人
else:
    if int(list2[0])>int(list1[1]):
        print(0)
    else:
        print(1)