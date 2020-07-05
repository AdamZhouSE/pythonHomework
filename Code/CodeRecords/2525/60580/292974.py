import heapq
import itertools

startTime = eval(input())
endTime = eval(input())
profit = eval(input())
H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
re = 0
while H:
    t = heapq.heappop(H)
    if t[1]:
        heapq.heappush(H, (t[2], 0, re + t[3]))
    else:
        re = max(re, t[2])
print(re)
