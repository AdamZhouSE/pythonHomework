words = eval(input())
res = []
log = []
for i in range(0,len(words)):
    tem = []
    log.append(words[i])
    tem.append(words[i])
    for j in range(i,len(words)):
        if words[j] in log:
            continue
        count = 0
        for h in range(0,len(words[0])):
            if words[i][h]!=words[j][h]:
                count+=1
        if count == 2:
            tem.append(words[j])
    res.append(tem)
mark = len(res)
for i in range(0,len(res)):
    m = 0
    for j in range(0,len(res[i])):
        for k in range(0,i):
            if res[i][j] in res[k]:
                mark-=1;
                m = 1
                break
        if m:
            break
print(mark)