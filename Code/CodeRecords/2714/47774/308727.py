maxl,maxn=110,1001
head=[-1 for i in range(maxl)]
ver=nex=len=ans=pre=[-1 for i in range(maxn)]
split=[[-1 for i in range(26)] for j in range(maxn)]
ch=[[-1 for i in range(maxn)] for j in range(maxl)]
mres,maid=0,-1
def addedge(len,id):
    ver[tot]=id
    nex[tot]=head[len]
    head[len]=tot
    tot+=1
def check(x,y):
    for i in range(26):
        if split[x][i]<split[y][i]:
            return False
    return True
def dp(cur):
    ans[cur]=1
    i=head[len[cur]-1]
    while(i!=-1):
        if check(cur,ver[i]):
            if ans[ver[i]]==0:
                dp(ver[i])
            if ans[ver[i]]+1>ans[cur]:
                ans[cur]=ans[ver[i]] + 1
                pre[cur] = ver[i]
        i=nex[i]    
    if(ans[cur]>mres):
        mres=ans[cur]
        maid=cur
stack=[0 for i in range(10010)]
st=0
pc=-1
while(1):
    try:
        ch[pc]=str(input())
        pc+=1
        len[pc] = strlen(ch[pc])
        for i in range(len[pc]):
            split[pc][ord(ch[pc][i])-ord('a')]+=1
        addedge(len[pc], pc)
    except:
        break
for i in range(pc+1):
    if ans[i]:
        continue
    dp(i)
print(mres)
a=maid
while(a!=-1):
    stack[st]=i
    st+=1
    a=pre[i]
for i in range(st-1,-2,-1):
    print(ch[stack[i]])
    
    
    
    