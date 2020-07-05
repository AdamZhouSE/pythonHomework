str1=input("")
str2=input("")
list1=str1.split( )
list2=str2.split( )
x=0
y=0
for i in list2:
    if int(i)>int(list1[1]):
        x=list2.index(i)
        break;
list2.reverse()
for j in list2:
    if int(j)>int(list1[1]):
        y=list2.index(j)
        break;
y=len(list2)-y
if len(list2)>1:
    if(y-x==len(list2)):
        print(len(list2))
    else:
        print(len(list2)-(y-x))
else:
    if int(list2[0])>int(list1[1]):
        print(1)
    else:
        print(0)

