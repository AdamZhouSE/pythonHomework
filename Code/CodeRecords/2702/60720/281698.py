list0=[]
while True:
    try:
        list0.append(list(input()))
    except:
        break
print(list0)
alen=len(list0)
blen=len(list0[0])
visit=[[0 for i in range(blen)] for j in range(alen)]
def dfs(a,b):
    if  list0[a][b]=='1':
        list0[a][b]=0
        if a>0:
            dfs(a-1,b)
        if b>0:
            dfs(a,b-1)
        if a<alen-1:
            dfs(a+1,b)
        if b<blen-1:
            dfs(a,b+1)
    else:
        return
sum=0
for i in range(alen):
    for j in range(blen):
        if list0[i][j]=='1':
            dfs(i,j)
            sum+=1
print(sum)