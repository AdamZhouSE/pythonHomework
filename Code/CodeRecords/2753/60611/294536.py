n=int(input())
flights=list(eval(input()))
src=int(input())
dst=int(input())
K=int(input())
from collections import defaultdict, deque
flights_dict = defaultdict(list)

visited = defaultdict(bool)
for flight in flights:
    flights_dict[flight[0]].append((flight[1], flight[2]))

queue = deque()
queue.appendleft((src, 0, 0))
min_price = float('inf')
while queue:
    for _ in range(len(queue)):
        start, counter, cur_price = queue.pop()
        for end, price in flights_dict[start]:
            # 到达目的地
            if end == dst and counter <= K:
                min_price = min(min_price, (cur_price + price))
            elif counter <= K and (cur_price + price) < min_price:
                queue.appendleft((end, counter + 1, cur_price + price))

if min_price != float('inf') :
    print(min_price )
else:
    print(-1)