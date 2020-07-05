n=int(input())
points=[]
for i in range(0,n):
    points.append([int(k) for k in input().split(",")])
max=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            temp=points[i][0]*points[j][1]-points[i][0]*points[k][1]+points[j][0]*points[k][1]-points[j][0]*points[i][1]+points[k][0]*points[i][1]-points[j][0]*points[j][1]
            if temp>max:
                max=temp
print(max)