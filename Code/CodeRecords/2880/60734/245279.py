lst = list(input().split(' '))
n = int(lst[0])
k = int(lst[1])

weight = list(input().split(' '))
weight = list(map(int,weight))

for i in range(n):
    if weight[i]<=k:
        weight[i] = 0
    else:
        break
for i in range(n-1,0,-1):
    if weight[i]<=k:
        weight[i] = 0
    else:
        break
print(weight.count(0))