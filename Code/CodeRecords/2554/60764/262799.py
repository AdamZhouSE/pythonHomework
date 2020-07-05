def evalTime(savior):
    i,j=0,0
    while i<len(savior)-1:
        j=i+1
        while j<len(savior):
            if min(savior[i][1],savior[j][1])>=max(savior[i][0],savior[j][0]):
                savior[i]=[min(savior[i][0], savior[j][0]),max(savior[i][1], savior[j][1])]
                savior.pop(j)
                j=i+1
            else:
                j+=1
        i+=1
    res=0
    for k in range(len(savior)):
        res+=savior[k][1]-savior[k][0]
    return res

n=int(input())
savior=[]
for i in range(n):
    savior.append(list(map(int,input().split())))
res=0
for i in range(n):
    tem=evalTime(savior[0:i]+savior[i+1:n])
    if tem>res:
        res=tem
print(res,end="")