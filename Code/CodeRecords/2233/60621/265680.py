a=eval(input())
grid=[]
for i in range(a):
    grid.append([int(x) for x in input().split()]+[i])

# valid=[False for i in range(a)]
# def dfs(i,set):
#     global valid,grid
#     valid[i]=True
#     grid[set][i]=1
#     for j in range(a):
#         if grid[i][j]==1 and valid[j]==False:
#             dfs(j,set)
# for i in range(a):
#     valid = [False for i in range(a)]
#     dfs(i,i)
# mimum=a
# def dp(i,depth,path:list):
#     global valid,mimum
#     if depth>mimum:
#         return
#     if i>=a:
#         valid = [False for j in range(a)]
#         for k in path:
#             if valid[k]==False:
#                 dfs(k)
#             else:
#                 depth-=1
#         if all(valid):
#             mimum=min(mimum,depth)
#         return
#     else:
#         dp(i+1,depth,path)
#         path.append(i)
#         dp(i+1,depth+1,path)
#         path.remove(i)
# dp(0,0,[])
# print(mimum)

df=[-1 for i in range(a)]
low=[-1 for i in range(a)]
queue=[]
belong=[-1 for i in range(a)]
index=-1
array=[]
connect=[i for i in range(a)]
def super(i):
    global df,low,queue,index,belong,array,connect
    
    df[i]=i
    low[i]=i
    queue.append(i)
    connect.remove(i)
    for j in range(a):
        if grid[i][j]==1:
            if df[j]==-1:
                super(j)
                low[i]=min(low[j],low[i])
            elif j in queue:
                low[i]=min(low[j],low[i])
    if low[i]==df[i]:
        index+=1
        t=queue.pop()
        temp=[i]
        while t!=i:
            temp.append(t)
            low[t]=low[i]
            belong[t]=low[i]
            t=queue.pop()
        array.append([x for x in temp])
def Maxi(ele,j,flag):
    maxi=ele[0]

    return maxi


while len(connect)!=0:
    t=connect[0]
    super(t)
total=0
if len(array)==0:
    for i in range(a):
        lis=i
        flag=True
        for j in range(a):
            if grid[j][i]==1:
                flag=False
                break
        if flag:
            total += 1

for k in range(len(array)):
    lis=array[k]
    flag=True
    for i in lis:
        if flag==False:
            break
        for j in range(a):
            if grid[j][i]==1 and j not in lis:
                flag=False
                break
    if flag:
        total+=1

print(total)

