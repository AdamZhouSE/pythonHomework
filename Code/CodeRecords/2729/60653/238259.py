import re;
s = list([int(n) for n in re.findall(r"\d+", input())])
for i in s:
    if s.count(i) == 1:
        print(i)
        break
