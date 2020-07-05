'''
你打算利用空闲时间来做兼职工作赚些零花钱。
这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
注意，时间上出现重叠的 2 份工作不能同时进行。
如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
'''

import itertools
import heapq

inp1 = input()
startTime = inp1[1:len(inp1)-1].split(",")
startTime = list(map(int, startTime))
inp2 = input()
endTime = inp2[1:len(inp2)-1].split(",")
endTime = list(map(int, endTime))
inp3 = input()
profit = inp3[1:len(inp3)-1].split(",")
profit = list(map(int, profit))

H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
res = 0
while H:
    tmp = heapq.heappop(H)
    if tmp[1]:
        heapq.heappush(H,(tmp[2],0,res+tmp[3]))
    else:
        res = max(res,tmp[2])
print(res)