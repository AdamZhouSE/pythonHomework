def nearest(list2,i,j):
    if list2[i][j]==0:
        return 0
    elif i==0and j==0:
        list2[i][j]=min(list2[0][1],list2[1][0])+1
        return list2[i][j]
    elif i==0and j==1:
        list2[i][j]=min(nearest(list2,0,0),nearest(list2,0,2))+1
        return list2[i][j]
    elif i==0and j==2:
        list2[i][j]=min(list2[0][1],list2[1][2])+1
        return list2[i][j]
    elif i==1and j==0:
        list2[i][j]=min(nearest(list2,0,0),nearest(list2,2,0))+1
        return list2[i][j]
    elif i==1and j==1:
        list2[i][j]=min(nearest(list2,1,0),nearest(list2,1,2),nearest(list2,0,1),nearest(list2,2,1))+1
        return list2[i][j]
    elif i==1and j==2:
        list2[i][j]=min(nearest(list2,0,2),nearest(list2,2,2))+1
        return list2[i][j]
    elif i==2and j==0:
        list2[i][j]=min(list2[2][1],list2[1][0])+1
        return list2[i][j]
    elif i==2and j==2:
        list2[i][j]=min(list2[2][1],list2[1][2])+1
        return list2[i][j]
    elif i==2and j==1:
        list2[i][j]=min(nearest(list2,2,0),nearest(list2,2,2))+1
        return list2[i][j]  

list2=eval(input())
flag0=0
flag1=0
for i in range(0,3):
    for j in range(0,3):
        if list2[i][j]==1:
            flag1+=1
        else:
            flag0+=1
for i in range(0,3):
    for j in range(0,3):
        if list2[i][j]==1:
            list2[i][j]=0
        else:
            list2[i][j]=999
for i in range(0,3):
    for j in range(0,3):
        nearest(list2,i,j)
maxx=-1
for i in range(0,3):
    for j in range(0,3):
        maxx=max(maxx,list2[i][j])
if flag0==0 or flag1==0:
    maxx=-1
print(maxx)