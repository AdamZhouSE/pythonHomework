import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
s.sort()
ans = min(s)
print(ans)