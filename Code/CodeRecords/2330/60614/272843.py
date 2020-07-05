num=int(input())
points=[]
minimum=1000
for i in range(num):
    points.append(eval('['+input()+']'))
for i in range(num-1):
    for j in range(i+1,num):
        mid=[(points[i][0]+points[j][0])/2,(points[i][1]+points[j][1])/2]
        doubleLen=pow((points[i][0]-mid[0]),2)+pow((points[i][1]-mid[1]),2)
        for k in range(num):
            if k!=i and k!=j:
                if pow(points[k][1]-mid[1],2)+pow(points[k][0]-mid[0],2)==doubleLen:
                    if [2*mid[0]-points[k][0],2*mid[1]-points[k][1]] in points:
                        temp=pow(pow(points[k][0]-points[j][0],2)+pow(points[k][1]-points[j][1],2),0.5)*pow(pow(points[k][0]-points[i][0],2)+pow(points[k][1]-points[i][1],2),0.5)
                        if temp<minimum:
                            minimum=temp
print('%.4f' % minimum)