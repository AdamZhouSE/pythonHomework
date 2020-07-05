n = int(input())
numLst = list(map(int,input().split(' ')))
numSet = []
newLst = []
for i in range(n - 1,-1,-1):
    if(numLst[i] not in numSet):
        numSet.append(numLst[i])
        newLst.insert(0,numLst[i])
result = ''
print(len(newLst))
for num in newLst:
    result = result + str(num) + ' '
print(result[:-1])