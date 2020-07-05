def similar(a,b):
    dif = []
    for i in range(len(a)):
        if a[i:i+1] != b[i:i+1]:
            dif.append(i)
    if len(dif)==0 or len(dif)==2:
        return True
    else:
        return False
    
import re
lst = re.findall(r'"(.*?)"',input())
relation = [-1]*len(lst)
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if similar(lst[i],lst[j]):
            relation[j] = i
print(relation.count(-1))