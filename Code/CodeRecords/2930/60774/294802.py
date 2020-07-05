n = int(input())
numLst = list(map(int,input().split(' ')))
count = 0
for i in range(1,n - 1):
    if((numLst[i] > numLst[i - 1] and numLst[i] > numLst[i + 1]) or (numLst[i] < numLst[i - 1] and numLst[i] < numLst[i + 1])):
        count = count + 1
print(count)