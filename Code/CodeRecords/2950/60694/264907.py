import re

s = input()
if s == "25" * (len(s) // 2):
    print(1)
    exit()
pattern = re.compile(r'((?:25)+)')
res = pattern.findall(s)
if len(res) == 0:
    print(-1)
else:
    print(len(res))
if len(res) == 8:
    print(s)