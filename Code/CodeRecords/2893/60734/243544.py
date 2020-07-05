import re
lst = list(re.findall(r'\d+',input()))
lst = list(map(int,lst))

for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
        print(lst[i])
        break