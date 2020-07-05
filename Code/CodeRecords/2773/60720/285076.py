import re
list0=[]
s=input()
while True:
    tmp=re.findall(r'\d+',input())
    l=len(tmp)
    if(l==0): break
    list0.append(list(map(int,tmp)))
n=len(list0)
visit=[[1 for i in range(n)] for j in range(n)]
seq=[]
for i in range(n):
    for j in range(n):
        lst=[list0[i][j],i,j]
        seq.append(lst)
seq.sort()
for i in range(len(seq)):
    x=seq[i][1]
    y=seq[i][2]
    maxn=visit[x][y]
    if x>0 and list0[x-1][y]<list0[x][y]:
        maxn=max(maxn,visit[x-1][y]+1)
    if y>0 and list0[x][y-1]<list0[x][y]:
        maxn=max(maxn,visit[x][y-1]+1)
    if x<n-1 and list0[x+1][y]<list0[x][y]:
        maxn=max(maxn,visit[x+1][y]+1)
    if y<n-1 and list0[x][y+1]<list0[x][y]:
        maxn=max(maxn,visit[x][y+1]+1)
    visit[x][y]=maxn
result=0
for i in range(n):
    result=max(result,max(visit[i]))
print(result)