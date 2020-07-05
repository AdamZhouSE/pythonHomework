def safe(comb,a):
    string = ''.join(comb)
    for i in range(len(a)):
        if a[i:i+1] in string:
            return False
    return True
    
def relate(comb,index):
    if index == len(lst):
        return
    
    for i in range(index,len(lst)):
        if safe(comb,lst[i]):
            comb.append(lst[i])
            res.append(comb.copy())
            relate(comb,i+1)
            comb.pop()
    
import re
lst = re.findall(r'"(.*?)"',input())
res = []
relate([],0)
max_len = 0
for x in res:
    s_len = len(''.join(x))
    if s_len>max_len:
        max_len = s_len
print(max_len)