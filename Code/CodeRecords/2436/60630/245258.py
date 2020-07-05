def combine(range1, range2) :
    if range1[1] < range2[0] :
        return range1
    return [range1[0], max(range1[1], range2[1])]

rangeList = input("")[2 : -2].split("],[")
rangeList = [[int(j) for j in i.split(',')] for i in rangeList]
newRange = [int(i) for i in input("")[1 : -1].split(',')]

i = 0
while i < len(rangeList) and rangeList[i][0] < newRange[0] :
    i += 1

if i > 0 and rangeList[i-1][1] >= newRange[0] :
    i -= 1
    rangeList[i] = combine(rangeList[i], newRange)
else :
    rangeList.insert(i, newRange)
while i < len(rangeList) - 1 and rangeList[i][1] >= rangeList[i+1][0] :
    rangeList[i] = combine(rangeList[i], rangeList[i+1])
    del rangeList[i+1]

print(rangeList)
