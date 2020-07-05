n=int(input())
points=[]
for a in range(n):
    point=list(map(int,input().split(',')))
    points.append(point)
s=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            tem1=points[i][0]*points[j][1]+points[j][0]*points[k][1]+points[k][0]*points[i][1]
            tem2=points[i][0]*points[k][1]+points[j][0]*points[i][1]+points[k][0]*points[j][1]
            tem=abs((tem1-tem2)/2)
            if tem>s:
                s=tem
print(s)