n=(int)(input())
position=[]
for i in range(n):
    position.append(list(map(int,input().split(' '))))
sum=0
for i in range(n):
    for j in range(i+1,n):
        m_distance=abs(position[i][0]+position[i][1]-position[j][0]-position[j][1])
        o_distance=pow(pow(position[i][0]-position[j][0],2)+pow(position[i][1]-position[j][1],2),1/2)
        if(m_distance==o_distance):
            sum+=1
print(sum)
