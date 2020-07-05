num=int(input())
list=[]
max=0
for i in range(num):
    list.append(input())
points=[]
for i in range(len(list)):
    points.append([int(list[i][0]),int(list[i][2])])

for i in range(len(list)-2):
    for j in range(i+1,len(list)-1):
        for k in range(j+1,len(list)):
            area=abs(points[i][0]*points[j][1]-points[j][0]*points[i][1]+points[j][0]*points[k][1]
                     -points[k][0]*points[j][1]+points[k][0]*points[i][1]-points[i][0]*points[k][1])/2
            if max<area: max=area
print(max)