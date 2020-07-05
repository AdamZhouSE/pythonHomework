import itertools
import heapq

inp1 = input()
start = inp1[1:len(inp1)-1].split(",")
start = list(map(int, start))
inp2 = input()
end = inp2[1:len(inp2)-1].split(",")
end = list(map(int, end))
inp3 = input()
profit = inp3[1:len(inp3)-1].split(",")
profit = list(map(int, profit))

H = sorted(zip(start, itertools.repeat(1), end, profit))
res = 0
while H:
    tmp = heapq.heappop(H)
    if tmp[1]:
        heapq.heappush(H,(tmp[2],0,res+tmp[3]))
    else:
        res = max(res,tmp[2])
print(res)