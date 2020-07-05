import re
import math
list1=re.split(',| |\[|\]',input())
list3=[]
for i in list1:
    try:
        list3.append(int(i))
    except:
        continue
print(int(math.log(len(list3),2)))