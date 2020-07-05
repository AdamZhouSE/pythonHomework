import re
string = input()
lst = re.findall(r'\d+',string)
for i in range(len(lst)):
    lst[i] = int(lst[i])
print(sorted(lst))