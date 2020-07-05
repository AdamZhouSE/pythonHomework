import collections
from typing import List
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            d[u].append(v)

        r = []
        def help(t):
            while d[t]:
                help(d[t].pop())
            r.append(t)
        help('JFK')
        return r[::-1]
ls=eval(input())
nls=[]
nls.append("JFK")
this=0
for i in range(len(ls)):
    nls.append(findItinerary(nls[i],ls))
print(findItinerary(nls[i],ls))