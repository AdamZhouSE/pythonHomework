info=list(eval(input()))
info.sort()
res=['JFK']
start,end=[],[]
for i in range(len(info)):
    start.append(info[i][0])
    end.append(info[i][1])
last=start.index('JFK')
for i in range(len(info)):
    temp=end[last]
    res.append(temp)
    del start[last]
    del end[last]
    if i==len(info)-1:
        break
    else:
        last=start.index(temp)
print(res)