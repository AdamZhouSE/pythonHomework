import re
s=re.findall(r"[0-9]{1,}",input())
x=int(s[0])
for i in range(1,x):
    r=str(x-i)
    if '0' in r or '0' in str(i):
        continue
    print([i,x-i])
    break