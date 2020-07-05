n = int(input())
points=[]
res=[]
start=[]
for i in range(0,n):
    p =input().split(' ')
    k = int(p[0])
    start.append(p[1])
    re =[]
    points.append(input().split(' '))
    for j in range(0,k):
        re.append(input().split(' ')[1:])
    res.append(re)
results =[]
for i in range(0,n):
    point = points[i]
    re =res[i]
    go = start[i]
    k = len(re[0])
    result =[go]
    m = point.index(go)
    while len(result)!=k:
        for j in range(0,k):
            if re[m][j] =='1' and point[j] not in result:
                result.append(point[j])
        m+=1
    results.append(result)

for i in range(0,len(results)):
    result = results[i]
    for j in range(0,len(result)-1):
        print(result[j],end=' ')
    print(result[len(result)-1])