temp=[int(x) for x in input().split(' ')]
s=temp[0]
p=temp[1]
pos=[]
for i in range(p):
    temp=[int(x) for x in input().split(' ')]
    pos.append(temp)
    
dis=[[-1]*p for i in range(p)]
def d(x1,y1,x2,y2):
    add=(x1-x2)**2+(y1-y2)**2
    return add**0.5
for i in range(p):
    for j in range(i+1,p):
        dis[i][j]=d(pos[i][0],pos[i][1],pos[j][0],pos[j][1])
        
union=[[i] for i in range(p)]
res=0
while(len(union)>s):
    m=-1
    x=0
    y=0
    for i in range(p):
        for j in range(i+1,p):
            if(m==-1):
                if(dis[i][j]!=-1):
                    m=dis[i][j]
                    x=i
                    y=j
            else:
                if(dis[i][j]<m and dis[i][j]!=-1):
                    m=dis[i][j]
                    x=i
                    y=j
    res=m
    dis[x][y]=-1
    i=0
    j=0
    k=0
    while(k<len(union)):
        if(x in union[k]):
            i=union[k]
        if(y in union[k]):
            j=union[k]
        k+=1
    if(i==j):
        continue
    temp=i+j
    union.remove(i)
    union.remove(j)
    union.append(temp)
    
print('%.2f'%res,end='')    
                    
        