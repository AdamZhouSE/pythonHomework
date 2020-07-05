num=int(input())
points=[]
for i in range(num):
    points.append([int(x) for x in input().split(',')])
maximum=2
for i in range(num):
    for j in range(i+1,num):
        temp=2
        if points[j][1]-points[i][1]==0:
            for k in range(num):
                if k!=i and k!=j and points[k][1]-points[i][1]==0:
                    temp+=1
        else:
            for k in range(num):
                if k!=i and k!=j and (points[j][0]-points[i][0])/(points[j][1]-points[i][1])==(points[k][0]-points[i][0])/(points[k][1]-points[i][1]):
                    temp+=1
        if temp>maximum:
            maximum=temp
print(maximum)