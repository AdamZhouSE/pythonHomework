import collections


def findItinerary( tickets) :
    d=collections.defaultdict(list)
    for u,v in sorted(tickets)[::-1]:
        d[u].append(v)
    r=[]
    def help(t):
        while d[t]:
            help(d[t].pop())
        r.append(t)
    help('JFK')
    return r[::-1]


tickets=input()
print(findItinerary(tickets))