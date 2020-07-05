R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
res=[]
for i in range(R):
    for j in range(C):
        res.append([i,j])
for i in range(R*C-1):
    for j in  range(i+1,R*C):
        former=abs(res[i][0]-r0)+abs(res[i][1]-c0)
        later = abs(res[j][0] - r0) + abs(res[j][1] - c0)
        if former>later:
            temp=res[i]
            res[i]=res[j]
            res[j]=temp
        if former==later and res[i][0]>res[j][0]:
            temp = res[i]
            res[i] = res[j]
            res[j] = temp
print(res)