num = int(input())
xlist = input().split(" ")
scores = [int(xlist[i]) for i in range(len(xlist))]

aSet = set(scores)
if 0 in aSet:
    aSet.remove(0)

print(len(aSet))
