a=input()
b=input()
c=eval(input())
flag=False
if b not in c:
    flag=True
c.insert(0,a)
c.append(b)
k=len(c)
d=[[False for i in range(k)] for j in range(len(c))]
valid=[k for i in range(k)]
t=[]
def diff(s1:str,s2:str):
    co=0
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            co+=1

    return co==1
j=0
for i in range(k):
    j=i+1
    while j<k:
        if(diff(c[i],c[j])):
            d[i][j]=True
            d[j][i]=True
        j+=1
def dp(x,depth,path:list):
    global length
    if (x==k-1):
        for j in range(len(path)):
            valid[path[j]]=j
            length=min(length,len(path))
        t.append([x for x in path])
    path.append(x)

    for i in range(k):
        if(d[x][i] and depth<=valid[i] and  i not in path):
            dp(i,depth+1,path)


    path.remove(x)
length=k
dp(0,0,[])
ans=[]
for i in t:
    if(len(i)==length):
        temp=[c[x] for x in i]
        temp.append(c[k-1])
        ans.append([x for x in temp])
#if ans==[['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]:
#    print(a,b,c)
if flag==True:
    ans=[]
print(ans)





