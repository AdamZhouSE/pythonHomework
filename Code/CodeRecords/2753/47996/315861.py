def findCheapestPrice(n, flights, src, dst, K):
    import collections
    flights_dict_end = collections.defaultdict(list)
    for flight in flights:
        flights_dict_end[flight[1]].append([flight[0], flight[2]])
    dp = [[float('inf') for i in range(n)] for i in range(K + 1)]
    for i in flights_dict_end[dst]:
        dp[0][i[0]] = i[1]
    for k in range(1, K + 1):
        for pos in range(n):
            for before in flights_dict_end[pos]:
                dp[k][before[0]] = min(dp[k][before[0]], dp[k-1][pos] + before[1])
            dp[k][pos] = min(dp[k][pos], dp[k-1][pos])
    ans = dp[K][src]
    return ans if ans != float('inf') else -1

n = int(input())
line = input()[1:-1].split("],")
src = int(input())
dst = int(input())
k = int(input())
edges = []
for i in range(n):
    if i != n-1:
        temp = [int(x) for x in line[i][1:].split(",")]
        edges.append(temp)
    else:
        temp = temp = [int(x) for x in line[i][1:-1].split(",")]
        edges.append(temp)
print(findCheapestPrice(n, edges, src, dst, k))
