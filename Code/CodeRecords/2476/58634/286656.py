import heapq

t = int(input())
for i in range(t):
    n = int(input())
    num = [int(i) for i in input().split(" ")]
    if len(num) == 1:
        print(num[0])
        continue
    heapq.heapify(num)
    res = 0
    while len(num) != 1:
        a = heapq.heappop(num)
        b = heapq.heappop(num)
        res += a+b
        heapq.heappush(num,a+b)
    print(res)