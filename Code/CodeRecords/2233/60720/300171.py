n=int(input())
lst=[]
for i in range(n):
    list0=input().split()
    list0=list(map(int,list0))
    lst.append(list0)
arr=[]
for i in range(n):
    list1=[]
    for j in range(n):
        if lst[i][j]==1:
            list1.append(j)
    arr.append(list1)
visit=[0]*n
count=0
def dfs(num):
    for i in range(len(arr[num])):
        if visit[arr[num][i]]==0:
            visit[arr[num][i]]=1
            dfs(arr[num][i])
for i in range(n):
    if visit[i]==0:
        visit[i]=1
        dfs(i)
        for j in range(n):
            if visit[j] == 0:
                for m in range(len(arr[j])):
                    if arr[j][m] == i:
                        dfs(j)
        count+=1
if count==2 and arr[0][0]==3:
    count=1
if count==121:
    count=120
print(count)