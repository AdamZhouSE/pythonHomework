import re
str=re.split(r'\s+',input())
str1=str[0];str2=str[1]

for i in range(min(len(str1),len(str2))):
    if str1[i]==str2[i]:
        pass
    else:
        print(ord(str1[i])-ord(str2[i]))
        break
    if i==len(str1):
        print(0)

