class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        dist = [[float('inf')] * n for _ in range(2)]
        dist[0][src] = dist[1][src] = 0

        for i in range(K+1):
            for u, v, w in flights:
                dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)

        return dist[K&1][dst] if dist[K&1][dst] < float('inf') else -1


if __name__ == "__main__":
    n = int(input())
    edges = eval(input())
    src = int(input())
    dst = int(input())
    k = int(input())
    s = Solution()
    res = s.findCheapestPrice(n, edges, src, dst, k)
    print(res)
