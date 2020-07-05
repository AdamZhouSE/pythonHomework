import re
str=input()
list=re.findall(r"[A-Za-z0-9]{1,}",str)
list1=list[0]
list2=list[1]
if(list2==list1):
    print(0)
for i in range(0,len(list1)):
    if(list1[i]==list2[i]):
        continue
    else:
        print(ord(list1[i])-ord(list2[i]))
        break