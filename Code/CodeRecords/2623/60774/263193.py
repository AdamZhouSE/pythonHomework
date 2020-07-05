numLst = list(map(int,input().split(',')))
numLst = sorted(numLst)
k = int(input())
print(numLst[-k])