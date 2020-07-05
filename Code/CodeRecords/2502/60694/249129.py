import sys
n = int(input())
l = []
cost = 0
for i in range(n):
    l.append(int(input()))
minCost = sys.maxsize
minIndex = 0
for j in range(n-1):
    for i in range(len(l) - 1):
        if minCost > max(l[i], l[i + 1]):
            minCost = max(l[i], l[i + 1])
            minIndex = i
    cost += minCost
    l.remove(min(l[minIndex], l[minIndex+1]))
print(cost)
