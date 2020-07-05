import re
import bisect
n = int(input())
if n == 1:
    print([-1])
else:
    lst = []
    for i in range(0, n):
        lst.append(list([int(n) for n in re.findall(r"\-?\d+", input())]))
    dic = {}
    for i, (start, end) in enumerate(lst):
        dic[start] = i
    res = [-1 for _ in range(len(lst))]
    l = [interval[0] for interval in lst]
    le = sorted(l, key=lambda x: x)
    for i, (start, end) in enumerate(lst):
        idx = bisect.bisect_left(le, end)
        if idx < len(le):
            res[i] = dic[le[idx]]
    print(res)