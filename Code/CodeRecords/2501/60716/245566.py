num = int(input())
ordarrange = input().split(' ')
aftarrange = input().split(' ')
dicts = dict()
index = 0
for i in ordarrange:
    dicts[i]=index
    index+=1
laterarr = list()
for i in afterarrange:
    x = dicts[i]
    laterarr.append(x)
indexs = 0
for i in range(len(laterarr)):
    for j in range(i+1,len(laterarr)):
        if laterarr[i]>laterarr[j]:
            indexs+=1
print(indexs)