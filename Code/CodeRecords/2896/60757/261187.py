s1=input()
str1=''
s2=input()
str2=''
s1=s1.split()
s2=s2.split()
for i in range(len(s1)):
    str1 = str1+s1[i]
for i in range(len(s2)):
    str2 = str2+s2[i]   
if len(str1)<len(str2) :
    print('NO',end='')
for i in range(len(str2)):
    found=0
    for j in range(len(str1)):
        if str2[i]==str1[j]:
            str1=str1[:j]+str1[j+1:]
            found=1
            break
    if found==0 :
        print('NO',end='')
        break
    elif i==len(str2)-1:
        print('YES',end='')
           