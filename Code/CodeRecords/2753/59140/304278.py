from collections import defaultdict, deque

n = int(input())
temp = input()
src = int(input())
dst = int(input())
k = int(input())
flights = [x.split(",") for x in temp[2:len(temp) - 2].split("],[")]
flights=[[int(x) for x in y] for y in flights]
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
            if end == dst and counter <= k:
                min_price = min(min_price, (cur_price + price))
            elif counter <= k and (cur_price + price) < min_price:
                queue.appendleft((end, counter + 1, cur_price + price))

if min_price != float('inf'):
    print(min_price)
else:
    print(-1)