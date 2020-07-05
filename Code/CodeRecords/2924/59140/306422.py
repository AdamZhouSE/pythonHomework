def countavg():
    result = 0
    for i in res:
        result += i[1]
    return result / len(res)


temp = [int(x) for x in input().split(" ")]
n, r, avg = temp[0], temp[1], temp[2]
res=[]
for _ in range(n):
    temp = [int(x) for x in input().split(" ")]
    res.append([temp[1],temp[0]])
res.sort()
index=0
result=0
while countavg()<avg:
    if res[index][1]<r:
        res[index][1]+=1
        result+=res[index][0]
    else:
        index+=1
print(result)
