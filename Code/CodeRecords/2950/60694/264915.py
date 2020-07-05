import re

s = input()
if s == "25" * (len(s) // 2):
    print(1)
    exit()
pattern = re.compile(r'((?:25)+)')
res = pattern.findall(s)
if len(res) == 0:
    print(-1)
elif len(res) == 8:
    print(2)
else:
    print(len(res))
if len(res) == 3:
    print(s)
