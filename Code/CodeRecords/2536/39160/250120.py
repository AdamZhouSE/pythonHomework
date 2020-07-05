import sys, os, io, collections

tickets = eval(input())

paths = collections.defaultdict(list)

for start, tar in tickets:
    paths[start].append(tar)
for start in paths:
    paths[start].sort(reverse=True)
s = []

def search(start):
    while paths[start]:
        search(paths[start].pop())
    s.append(start)

search("JFK")
print(s[::-1])