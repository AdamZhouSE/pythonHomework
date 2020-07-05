import re;
a = input()
r = [int(n) for n in re.findall(r"\d+", input())]
n = r[0]
m = r[1]
k = r[2]
s = list([int(n) for n in re.findall(r"\d+", input())])
t = list([int(n) for n in re.findall(r"\d+", input())])
for i in t:
    s.append(i)
s.sort()
print(s[k-1])