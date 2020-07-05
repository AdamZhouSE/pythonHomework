def dfs(a,b):
    if arr[a][b]=='0': return
    if visit[a][b]==0: visit[a][b]=1
    else: return
    if(a>0): dfs(a-1,b)
    if(a<lena-1): dfs(a+1,b)
    if(b>0): dfs(a,b-1)
    if(b<lenb-1): dfs(a,b+1)

arr=[]
while True:
    try:
        arr.append(list(input()))
    except:
        break
lena=len(arr)
lenb=len(arr[0])
visit=[[0 for i in range(lenb)]for j in range(lena)]
ans=0
for i in range(lena):
    for j in range(lenb):
        if(arr[i][j]=='1' and visit[i][j]==0): 
            dfs(i,j)
            ans+=1
print(ans)
