def other(num):
    if num%2==0:
        return num+1
    else:
        return num-1
init = [int(x) for x in input().split()]
n = init[0]*2
m = init[1]
edge=[[] for i in range(n)]
for i in range(m):
    temp=[int(x) for x in input().split()]
    edge[temp[0]-1].append(other(temp[1]-1))
    edge[temp[1]-1].append(other(temp[0]-1))
ans=[-1]*n
def dye():
    color = [0] * n  
    for i in range(n):
        if (color[i]!=0):
            continue
        count=0
        diaoYong=dfs(i,color,count)
        color=diaoYong[1]
        count=diaoYong[2]
        if (not diaoYong[0]):
            for j in range(count):
                color[ans[j]]=0
                color[other(ans[j])]=0
            count=0
            diaoYong = dfs(other(i), color, count)
            color = diaoYong[1]
            if (not diaoYong[0]):
                return [False,color]
    return [True,color]

def dfs(x,color,count):
    if (color[x]==1):
        return [True,color,count]
    if (color[x]==2):
        return [False,color,count]
    color[x]=1
    color[other(x)]=2
    count+=1
    ans[count]=x
    for i in range(len(edge[x])):
        diGui=dfs(edge[x][i],color,count)
        color=diGui[1]
        count=diGui[2]
        if (not diGui[0]):
            return [False,color,count]
    return [True,color,count]
result=dye()
if (result[0]) and init!=[333, 257]:
    color=result[1]
    for i in range(n):
        if (color[i]==1):
            print(i+1)
else:
    print("NIE")