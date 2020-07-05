s = input()
t = input()
sList = list(s)
sList.sort()
sortedS = ''
for i in sList:
    sortedS += i

if sortedS in sList:
    startIndex = t.find(sortedS)
    t.replace(t[startIndex:startIndex+len(s)], s)

print(t)