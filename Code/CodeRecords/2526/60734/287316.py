import re
lst = []
for line in iter(input,''):
    lst.append(list(map(int,re.findall(r'\d+',line))))
print(sorted(lst))