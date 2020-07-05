#贪心，找需要写论文最少的，写到分最大
import heapq
n, r, avg = map(int, input().split())
h = []
h1 = []
for i in range(n):
    temp = list(map(int, input().split()))
    if r - temp[0] > 0:
        heapq.heappush(h, [temp[1], r - temp[0]])
    h1.append(temp[0])
h.sort()
h.reverse()
s = sum(h1)
x = n * avg - s
ans = 0

while x > 0:
    temp = h.pop()
    if temp[1] > x:
        ans += temp[0] * x
        x = 0

    else:
        x -= temp[1]
        ans += temp[0] * temp[1]
print(ans)