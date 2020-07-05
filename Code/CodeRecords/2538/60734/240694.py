import re
lst = input()
lst = re.findall(r'\d+',lst)
for i in range(len(lst)):
    lst[i] = int(lst[i])
lst.sort()
if lst[0] != 0:
    lst.insert(0,0)

res = 0
for i in range(1,len(lst)):
    if lst[i] != i:
        res = i
        break
if res == 0:
    res = len(lst)
print(res)