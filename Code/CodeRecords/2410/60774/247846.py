import copy

numLst = list(map(int,input().split(',')))
diff = int(input())
record = []
for n in range(0,len(numLst)):
    i = numLst[n]
    temp = [i]
    numLstCopy = copy.deepcopy(numLst[n:])
    while((i + diff) in numLstCopy):
        numIndex = numLstCopy.index(i + diff)
        numLstCopy = numLstCopy[numIndex:]
        temp.append(i + diff)
        i = i + diff
    record.append(temp)
longest = 0
for item in record:
    if(len(item) > longest):
        longest = len(item)
print(longest)