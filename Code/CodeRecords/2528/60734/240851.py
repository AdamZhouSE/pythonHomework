import re
lst = re.findall(r'\d+',input())
lst = list(map(int,lst))
print(sorted(lst))