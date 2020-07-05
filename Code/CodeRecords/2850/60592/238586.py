total = int(input())
index = 0
rec = []
data = list(map(int,input().split(' ')))
i = 0
while i < total:
    if data[i]==0:
        rec.append(i)
        j = i+1
        while j<total and data[j]==0:
            j+=1
        i = j
maxs = []
for i in range(0,len(rec)):
    start = rec[i]
    ma = 0
    mark = 0
    for j in range(start,total):
        if data[j] == 0:
            mark+= 1
        else:
            mark-=1
        if mark > ma:
            ma = mark
    maxs.append(ma)
maxs.sort()
print(sum(data)+maxs[len(maxs)-1])