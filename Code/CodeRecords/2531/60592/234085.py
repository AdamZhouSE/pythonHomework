tem = list(input())
tem.sort()
i = 0
res = []
index = []
str = ""
while i < len(tem):
    count = 0
    j = i
    while(j<len(tem) and tem[i] == tem[j]):
        j+=1
        count+=1
    res.append(count)
    i = j
for i in range(0,len(res)):
    max = 0
    mark = 0
    for k in range(0,len(res)):
        if res[k] >= max and not (k in index):
            max = res[k]
            mark = k
    index.append(mark)
chain = list(set(tem))
chain.sort(key=tem.index)
for i in range(0,len(res)):
    str += res[index[i]]*chain[index[i]]
print(str)