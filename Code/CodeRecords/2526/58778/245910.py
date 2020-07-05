s1=input()
s1=s1[1:len(s1)-1]
s2=input()
s2=s2[1:len(s2)-1]
l1=s1.split(',')
l2=s2.split(',')
list1=[]
for i in l1:
    if(i[0:1]==' '):
        list1.append(int(i[1:]))
    else:
        if(i!='null' and i!=''):
            list1.append(int(i))
for i in l2:
    if (i[0:1] == ' '):
        list1.append(int(i[1:]))
    else:
        if(i!='null' and i!=''):
            list1.append(int(i))
list1.sort()
print(list1)
