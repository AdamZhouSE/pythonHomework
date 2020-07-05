points=list(eval(input()))
k=int(input())
res=[]
for i in range(k):
    ind=0
    dis=pow(points[0][0],2)+pow(points[0][1],2)
    for j in range(len(points)):
        if pow(points[j][0],2)+pow(points[j][1],2)<dis:
            ind=j
            dis=pow(points[j][0],2)+pow(points[j][1],2)
    res.append(points.pop(ind))
print(res)