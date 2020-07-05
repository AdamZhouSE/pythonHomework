import re
#for i, j in enumerate(s):
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
s.sort()
print(s)