import re;
s = list([int(n) for n in re.findall(r"\d+", input())])
n = len(s)
t = n / 3
ans = []
for i in s:
    if s.count(i) > t and ans.count(i) == 0:
        ans.append(i)
print(ans)