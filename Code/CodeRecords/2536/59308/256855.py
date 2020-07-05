import re
from collections import defaultdict
from bisect import bisect_left

title = input()
pattern = re.compile('[A-Z]+')
result = pattern.findall(title)
time_table = [[result[i], result[i+1]] for i in range(0, len(result), 2)]
dest = defaultdict(list)
for i, j in time_table:
    dest[i] += [j]
for i in dest:
    dest[i].sort()
ans = ['JFK']
f_ = 'JFK'
while dest[f_]:
    f_ = dest[f_].pop(0)
    ans.append(f_)
print(ans)


