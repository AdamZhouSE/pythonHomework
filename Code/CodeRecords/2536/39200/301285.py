import collections

string = input()
B = string[2:-2:1].replace(' ','').split("],[")
tickets = []
for A in B:
    tickets.append(A.replace('"','').split(","))

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
