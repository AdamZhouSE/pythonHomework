s = input()
s = s[1:len(s)-1].replace('"', '')
s = s.split(",")
d = set()
flag = True
for c in s:
    k = int(c[: 2]) * 60 + int(c[3:])
    if k in d:
        flag = False
        break
    d.add(k)
if flag:
    d = sorted(d)
    d.append(d[0] + 1440)
    print(min(d[i] - d[i - 1] for i in range(1, len(d))))
else:
    print(0)
