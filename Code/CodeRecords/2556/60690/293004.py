str=input().split(" ")
n=int(str[0])
k=int(str[1])
point=[]
for i in range(n):
    str=input().split(" ")
    x=int(str[0])
    y=int(str[1])
    point.append([x,y])
res=[]
for i in range(n-1):
    for j in range(i+1,n):
        x1=point[i][0]
        y1=point[i][1]
        x2=point[j][0]
        y2=point[j][1]
        if abs(x1-x2)<6 and abs(y1-y2)<6:
            area=(6-abs(x1-x2))*(6-abs(y1-y2))
            res.append(area)
if len(res)==0:print(0)
elif len(res)==1:print(res[0])
else:print(-1)
