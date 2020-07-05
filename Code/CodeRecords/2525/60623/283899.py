import heapq
import itertools

startTime=eval(input())
endTime=eval(input())
profit=eval(input())
H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
res = 0
while H:
    t = heapq.heappop(H)
    if t[1]:
        heapq.heappush(H, (t[2], 0, res + t[3]))
    else:
        res = max(res, t[2])
print(res)

