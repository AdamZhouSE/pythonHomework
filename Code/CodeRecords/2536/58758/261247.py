pairs = eval(input())
pairs.sort()
ans = []
start = []
end = []
isvalid = [True for x in range(len(pairs))]
for city in pairs:
    start.append(city[0])
    end.append(city[1])
target = 'JFK'
for i in range(0, len(pairs)):
    ind = start.index(target)
    if not isvalid[ind]:
        while True:
            ind = start.index(target, ind+1)
            if isvalid[ind]:
                break
    ans.append(target)
    target = end[ind]
    isvalid[ind] = False
ans.append(target)
print(ans)
