inp=eval(input())
inp.sort()
res=['JFK']
for i in inp:
    if i[0]=='JFK':
        res.append(i[1])
        inp.pop(inp.index(i))
for i in inp:
    if res[len(res)-1]==i[0]:
        res.append(i[1])
print(res)