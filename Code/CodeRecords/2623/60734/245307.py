import re
lst = re.findall(r'\d+',input())
k = int(lst.pop(len(lst)-1))
lst = list(map(int,lst))
lst = sorted(lst,reverse = True)
print(lst[k-1])