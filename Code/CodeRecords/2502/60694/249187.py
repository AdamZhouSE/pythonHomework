import sys
n = int(input())
l = []
cost = 0
for i in range(n):
    l.append(int(input()))
for j in range(n-1):
    minCost = sys.maxsize
    minIndex = 0
    for i in range(len(l) - 1):
        if minCost > max(l[i], l[i + 1]):
            minCost = max(l[i], l[i + 1])
            minIndex = i
    cost += minCost
    if l[minIndex] > l[minIndex+1]:
        del l[minIndex+1]
    else:
        del l[minIndex]
print(cost)
