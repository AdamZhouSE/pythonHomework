import heapq as hq

heap = []
k, m = map(int, input().split())
hq.heappush(heap, 1)
anstr=[]
while k > 0:
    head = hq.heappop(heap)
    hq.heappush(heap, head * 2 + 1)
    hq.heappush(heap, head * 4 + 5)
    anstr.append(str(head))
    k = k - 1
s = ''.join(anstr)
print(s)
num = list(s)
while m > 0:
    for i in range(len(num)):
        if num[i] < num[min(i + 1,len(num) - 1)]:
            num.pop(i)
            m = m -1
            break
ans = ''.join(num)
print(ans, end='')