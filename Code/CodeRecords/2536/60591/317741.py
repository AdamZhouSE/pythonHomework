# -*- coding: utf-8 -*-
result = []
def find(now,n,paths,tempTo):
    if(n == 0):
        result.append(paths)
        return
    if(len(tempTo[now]) == 0):
        return
    for i in range(len(tempTo[now])):
        if(len(tempTo[now])==0):
            return
        temp = paths.copy()
        temp.append(tempTo[now][i])
        next = tempTo[now][i]
        tempF = tempTo.copy()
        del tempF[now][i]
        find(next,n - 1,temp,tempF)

airports = eval(input())
fromTo = {}
for line in airports:
    if(line[0] in fromTo):
        fromTo[line[0]].append(line[1])
        fromTo[line[0]].sort()
    else:
        fromTo[line[0]] = [line[1]]
paths = ['JFK']
paths = find('JFK',len(airports),paths,fromTo)
print(result[0])