import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = len(s)
set = sorted(list(set(s)), reverse=True)
for i in set:
    cl = [index for index in s if i <= index]
    if i <= len(cl):
        print(i)
        break