s = input()
if s == "25" * (len(s) // 2):
    print(1)
    exit()
cnt = 0
import re
pattern = re.compile(r'((?:25)+)')
res = pattern.findall(s)
print(len(res))
