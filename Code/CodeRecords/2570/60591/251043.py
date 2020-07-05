n = eval(input())
envelops = []
result = []
while(n != 0):
    n = n - 1
    envelop = list(map(int,input().split(",")))
    envelops.append(envelop)
    result.append([1])
envelops.sort()
for x in range(len(envelops)):
    for y in range(x + 1,len(envelops)):
        if(envelops[x][0] < envelops[y][0] and envelops[x][1] < envelops[y][1]):
            for temp in result[x]:
                if(1 + temp not in result[y]):
                    result[y].append(1 + temp)
fin = 0
for res in result:
    temp = max(res)
    if(temp > fin):
        fin = temp
print(fin)