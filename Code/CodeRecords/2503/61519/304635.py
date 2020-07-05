n=int(input())-1
tem=[]
for i in range(n):
    l=list(input().split(" "))
    tem.append(l)
res=[]
for i in range(n-1):
    for j in range(i+1,n):
        if tem[i][1]==tem[j][0]:
            tem[i][1]=tem[j][1]
for i in range(n-1):
    res.append(int(tem[i][1])-int(tem[i][0]))
print(max(res))