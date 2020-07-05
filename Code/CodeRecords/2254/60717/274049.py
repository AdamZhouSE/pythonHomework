def Warshall(edge,f):
    list1=[[0 for i in range(0,f)] for j in range(0,f)]
    list2=[[1 for i in range(0,f)] for j in range(0,f)]
    for i in edge:
        list1[i[0]][i[1]]=1
        list1[i[1]][i[0]]=1
    for i in range(0,f):
        list1[i][i]=1
    for i in range(0,f):
        for j in range(0,f):
            for k in range(0,f):
                if list1[i][j]==1 and list1[k][i]==1:
                    list1[k][j]=1
    if list1==list2:
        return True
    else:
        return False

tmp=input().split()
f=int(tmp[0])
r=int(tmp[0])
edge=[]
for i in range(0,r):
    tmp=input().split()
    a=int(tmp[0])-1
    b=int(tmp[1])-1
    edge.append([a,b])
count=0
for i in range(0,r):
    tmp=edge.pop(i)
    if Warshall(edge,f):
        count+=1
    edge.append(tmp)
if count%2==0:
    print(int(count/2))
else:
    print(int(count/2)+1)