list1=input()
list2=input()
str1=[]
str2=[]
for i in list1:
    str1.append(i)
for i in list2:
    str2.append(i)
c=0
for i in range(len(str2)):
    if str2[i]!=' ':
        a=0
        for j in range(len(str1)):
            if str2[i]==str1[j]:
                str1[j]=' '
                
                a=1
                break
        if a==0:
            c=1
            print('NO',end='')
            break
if c==0:
    print('YES',end='')