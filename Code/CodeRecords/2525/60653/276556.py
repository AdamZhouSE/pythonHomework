import re
import heapq
import itertools
startTime = list([int(n) for n in re.findall(r"\-?\d+", input())])
endTime = list([int(n) for n in re.findall(r"\-?\d+", input())])
profit = list([int(n) for n in re.findall(r"\-?\d+", input())])
H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
res = 0
while H:
    t = heapq.heappop(H)
    if t[1]:
        heapq.heappush(H, (t[2], 0, res + t[3]))
    else:
        res = max(res, t[2])
print(res)