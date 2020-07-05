t=int(input())

for i in range(t):
    temp=[int(x) for x in input().split(' ')]
    n=temp[0]
    m=temp[1]
    dis=temp[2]
    sell=[int(x) for x in input().split(' ')]
    road=[[-1]*n for j in range(n)]
    for j in range(m):
        temp=[int(x) for x in input().split(' ')]
        x=temp[0]-1
        y=temp[1]-1
        d=temp[2]
        road[x][y]=d
    temp=[int(x) for x in input().split(' ')]
    sou=temp[0]-1
    des=temp[1]-1
    best=[[-1,0,0] for j in range(n)]
    for j in range(n):
        if(sell[j]==1):
            best[j][1]+=1
        else:
            best[j][2]+=1
    al=[]
    pre=-1
    for j in range(n-1):
        ind=0
        lea=0
        for k in range(n):
            if(pre==-1 and abs(best[k][1]-best[k][2])<dis):
                best[k][0]=road[sou][k]
                if(sell[k]==1):
                    best[k][1]+=1
                else:
                    best[k][2]+=1
            else:
                if(road[pre][k]!=-1 and (road[pre][k]+best[pre][0])<best[k][0] and abs(best[pre][1]-best[pre][2])<dis):
                    best[k]=road[pre][k]+best[pre][0]
                    if(sell[j]==1):
                        best[j][1]+=1
                    else:
                        best[j][2]+=1
        for k in range(n):
            if(lea==0 and best[k][0]!=-1 and k not in al):
                lea=best[k][0]
                ind=k
            elif(lea!=0 and best[k][0]!=-1 and best[k][0]<lea and k not in al):
                lea=best[k][0]
                ind=k
        pre=ind
        
    print(best[des][0])
            