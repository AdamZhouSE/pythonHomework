import collections

t=int(input())
res=eval(input())
leng=len(res)
# 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# 输出：2
p=[i for i in range(t)]
def union(x,y):
    p[find(x)]=find(y)
def find(x):
    if(x!=p[x]):
        x=find(p[x])
    return x
tmp=collections.defaultdict(list)
if(t-1>leng):
    print("-1")
else:
    for i in range(leng):
        union(res[i][0],res[i][1])
    for i in range(leng):
        x=find(res[i][0])
        tmp[x].append(res[i][0])
        tmp[find(res[i][1])].append(res[i][1])
    linknum=0
    for i in tmp.keys():

        tmp[i]=list(set(tmp[i]))
        linknum+=len(tmp[i])
    ex=t-linknum
    if(len(res)-linknum+1<ex-1):
        print('-1')
    else:
        print(ex+len(tmp)-1)



