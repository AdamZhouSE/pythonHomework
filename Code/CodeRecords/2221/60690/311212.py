def dfs(this,key,dict):
    count=0
    for i in range(len(team)):
        if team[i][0]==key and team[i][1] not in this:
            this.append(team[i][1])
            count+=1
            dfs(this,team[i][1],dict)
    if count==0:return

s=input().split(" ")
N,M=int(s[0]),int(s[1])
team=[]
dict={}
for i in range(N):
    dict[i+1]=[]
for i in range(M):
    s=input().split(" ")
    team.append([int(s[0]),int(s[1])])
    dict[int(s[0])].append(int(s[1]))

for key in dict.keys():
    this=[]
    for e in dict[key]:
        dfs(this,e,dict)
    for e in this:
        if e not in dict[key]:
            dict[key].append(e)
res=0
for key in dict.keys():
    cur=key
    isAll=True
    for k in dict.keys():
        if k!=cur and cur not in dict[k]:
            isAll=False
            break
    if isAll:res+=1
print(res)