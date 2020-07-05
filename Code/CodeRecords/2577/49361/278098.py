import heapq
import itertools


class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
        res = 0
        while H:
            t = heapq.heappop(H)
            if t[1]:
                heapq.heappush(H, (t[2], 0, res + t[3]))
            else:
                res = max(res, t[2])
        return res

input1 = input().replace("\n", "").split(",")
for i in range(len(input1)):
    input1[i] = int(input1[i])
input2 = input().replace("\n", "").split(",")
for i in range(len(input2)):
    input2[i] = int(input2[i])
input3 = input().replace("\n", "").split(",")
for i in range(len(input3)):
    input3[i] = int(input3[i])

print(Solution().jobScheduling(input1, input2, input3))
