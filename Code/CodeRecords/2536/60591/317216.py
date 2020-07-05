# -*- coding: utf-8 -*-
result = []
def find(now,n,paths):
    if(n == 0):
        paths.append(now)
        result.append(paths)
        return
    if(now not in fromTo.keys()):
        return
    temp = paths.copy()
    temp.append(now)
    for next in fromTo[now]:
        find(next,n - 1,temp)

airports = eval(input())
fromTo = {}
for line in airports:
    if(line[0] in fromTo):
        fromTo[line[0]].append(line[1])
        fromTo[line[0]].sort()
    else:
        fromTo[line[0]] = [line[1]]
print(fromTo)

paths = []
paths = find('JFK',len(fromTo),paths)
print(*result[0])





