stones = eval(input())
count = 0
res = []
for i in range(0,len(stones)-1):
    res.append(stones[i])
    for j in range(i+1,len(stones)):
        if stones[j] in res:
            continue
        if stones[i][0]==stones[j][0] or stones[i][1] == stones[j][1]:
            res.append(stones[j])
            count+=1
print(count)
            
        