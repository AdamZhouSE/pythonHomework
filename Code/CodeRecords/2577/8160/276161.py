import itertools
import heapq
def jobScheduling(startTime, endTime, profit):
    H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
    res = 0
    while H:
        t = heapq.heappop(H)
        if t[1]:
            heapq.heappush(H, (t[2], 0, res + t[3]))
        else:
            res = max(res, t[2])
    return res


startTime=input()
endTime=input()
profit=input()
print(jobScheduling(startTime, endTime, profit))