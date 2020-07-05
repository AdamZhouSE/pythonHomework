import re
list1=re.split(',| |\[|\]',input())
list2=re.split(',| |\[|\]',input())
list3=[]
for i in list1:
    try:
        list3.append(int(i))
    except:
        continue
for i in list2:
    try:
        list3.append(int(i))
    except:
        continue
list3.sort()
print(list3)