import math
n=int(input())
for _ in range(n):
    m=int(input())
    point=[]
    for i in range(m):
        point.append(list(map(int,input().split())))
    count=0
    for i in range(m-1):
        for j in range(i+1,m):
            x1=point[i][0]
            y1=point[i][1]
            x2=point[j][0]
            y2=point[j][1]
            od=math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
            md=abs(x1-x2)+abs(y1-y2)
            if od==md:
                count+=1
    print(count)