row = int(input())
col = int(input())
threshold = int(input())
all = []
first = []
res=[]
for i in range(row):
    first.append(i+1)
for i in range(1,col+1):
    temp = first.copy()
    for k in range(len(temp)):
        temp[k] = i*temp[k]
    all.append(temp)
for i in all:
    for k in i:
        res.append(k)
res.sort()
print(res[threshold-1])
        