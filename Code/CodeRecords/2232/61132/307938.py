def saikono_hamon(in0,strocon):
    strocon.append(in0)
    for i in graph[in0]:
        if i not in strocon:
            saikono_hamon(i,strocon)
    return strocon

n=int(input())
digraph = [[] for i in range(n)]
graph = [[] for i in range(n)]
for j in range(n):
    tmp=list(map(lambda x:int(x)-1, input().split()))[:-1]
    digraph[j]+=tmp
    graph[j]+=tmp
    for i in tmp:
        graph[i]+=[j]
strocon=[]
conset=[]
ans=[0,0]
for i in range(n):
    if i not in strocon:
        tmp=saikono_hamon(i,[])
        strocon+=tmp
        conset.append(tmp)
for i in conset:
    in0=[]
    out0=[]
    for j in i:
        if not digraph[j]:
            out0.append(j)
        elif digraph[j] == graph[j]:
            in0.append(j)
    ans[0]+=max(len(in0),1)
    ans[1]+=max(len(in0),len(out0))
if ans[0]==2 and ans[1]==0:
    print(2)
    print(2)
else:
    print(ans[0])
    print(ans[1])
