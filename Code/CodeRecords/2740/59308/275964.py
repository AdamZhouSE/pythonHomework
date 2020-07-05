import re
pattern = re.compile('[0-9]+:[0-9]+')
s = pattern.findall(input())
d = set()
for i in s:
    k = int(i[:2])*60 + int(i[3:])
    if k in d:
        print(0)
        break
    else:
        d.add(k)
d = sorted(d)
d.append(d[0]+1440)
print(min(d[i] - d[i - 1] for i in range(1, len(d))))