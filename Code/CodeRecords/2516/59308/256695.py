import re
from bisect import  bisect_left

n = int(input())
set_ = list()
for i in range(n):
    pattern = re.compile('[0-9]+')
    a = [int(x) for x in pattern.findall(input())]
    set_.append([a[0], a[1], i])
s_set_ = sorted(set_, key=lambda x: x[0])
ans = []
for i in set_:
    j = bisect_left(s_set_, [i[1], float("-inf"), 0])
    if j == len(s_set_):
        ans.append(-1)
    else:
        ans.append(s_set_[j][-1])
print(ans)

