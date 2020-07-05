import re
s = list([str(n) for n in re.findall(r"[a-z]+", input())])
a = list(s[1])
b = list(s[3])
f = [False]*256
for i in a:
    f[ord(i)] = True
flag = True
for i in b:
    if f[ord(i)]:
        continue
    else:
        flag = False
        break
if flag:
    print("true")
else:
    print("false")