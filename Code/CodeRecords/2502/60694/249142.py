import sys
n = int(input())
l = []
cost = 0
for i in range(n):
    l.append(int(input()))
for j in range(n-1):
    cost += max(l[j], l[j+1])
print(cost)
