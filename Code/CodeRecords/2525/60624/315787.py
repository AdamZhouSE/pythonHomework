import heapq
import itertools
def func18():
    startTime = list(map(int, input().strip()[1:-1].split(",")))
    endTime = list(map(int, input().strip()[1:-1].split(",")))
    profit = list(map(int, input().strip()[1:-1].split(",")))
    H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
    res = 0
    while H:
        t = heapq.heappop(H)
        if t[1]:
            heapq.heappush(H, (t[2], 0, res + t[3]))
        else:
            res = max(res, t[2])
    print(res)
    return res
func18()