import collections

s = str(input()).strip('[""]').split('"')
place = []
for i in s:
    if len(i) == 3 and i.isalpha():
        place.append(i)
tickets = []
for i in range(0, len(place) - 1):
    if i % 2 == 0:
        temp = [place[i], place[i + 1]]
        tickets.append(temp)
d = collections.defaultdict(list)
for u, v in sorted(tickets)[::-1]:
    d[u].append(v)
    r = []


def help(t):
    while d[t]:
        help(d[t].pop())
    r.append(t)


help('JFK')
print(r[::-1])