n,g = [int(i) for i in input().split(' ')]
res = 0
change = []
milk = [g]*n

for i in range(n):
    temp = [int(i) for i in input().split(' ')]
    change.append(temp)
change.sort(key = lambda x: x[0])
ma = g
for i in range(n):
    index = change[i][1]-1
    temp = change[i][2]
    milk[index] += temp
    if ma != max(milk):
        res+=1
        ma = max(milk)
print(res,end='')