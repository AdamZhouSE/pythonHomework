def noCommon(a,b):
    for i in range(len(a)):
        if a[i:i+1] in b:
            return False
    return True
    
import re
lst = re.findall(r'"(.*?)"',input())

max_len = 0
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if noCommon(lst[i],lst[j]):
            words_len = len(lst[i])*len(lst[j])
            if words_len>max_len:
                max_len = words_len
print(max_len)