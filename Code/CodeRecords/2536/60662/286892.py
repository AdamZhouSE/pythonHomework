import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        d = collections.defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            d[u].append(v)

        r = []

        def help(t):
            # 注意从A出发, 又返回到A的情况.
            while d[t]:
                help(d[t].pop())
            r.append(t)

        help('JFK')
        return r[::-1]