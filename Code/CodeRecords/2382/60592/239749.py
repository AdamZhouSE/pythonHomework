total = int(input())
data = []
for i in range(0,total):
    ls = list(map(int,input().split(' ')))
    data.append(ls)
data.sort(key = (lambda x:x[0]))
res = []
i = 0
while i < total:
    left = data[i][0]
    right = data[i][1]
    while i+1 < total and data[i+1][0]<=right:
        right = data[i+1][1]
        i += 1
    res.append([left,right])
    i+=1
for i in range(0,len(res)):
    print(res[i][0],end=' ')
    print(res[i][1])