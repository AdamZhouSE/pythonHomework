import math
n=int(input())
distance=[]
for i in range(n):
    x=list(map(int,input().split()))
    distance.append(x)
count=0
for i in range(0,n):
    for j in range(i+1,n):
        x1=distance[i][0]
        y1=distance[i][1]
        x2=distance[j][0]
        y2=distance[j][1]
        o_dis=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
        m_dis=abs(x1-x2)+abs(y1-y2)
        if(o_dis==m_dis):
            count+=1
print(count)