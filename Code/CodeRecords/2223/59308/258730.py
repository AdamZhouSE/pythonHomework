import re
pattern = re.compile('-*[0-9]+')
a = [int(x) for x in pattern.findall(input())]
s = set()
res = list()
for i in range(len(a)):
    s.add(i+1)
for j in a:
    if j in s:
        s.remove(j)
    else:
        res.append(j)
res.append(s.pop())
print(res)



