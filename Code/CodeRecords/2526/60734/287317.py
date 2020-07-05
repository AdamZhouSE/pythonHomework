import re
lst = []
try:
    for line in iter(input,''):
        lst.append(list(map(int,re.findall(r'\d+',line))))
except:
    pass
print(sorted(lst))