def saikono_hamon(in0,strocon):
    strocon.append(in0)
    for i in graph[in0]:
        if i not in strocon:
            saikono_hamon(i,strocon)

n=int(input())
digraph = [[] for i in range(n)]
graph = [[] for i in range(n)]
for j in range(n):
    tmp=list(map(lambda x:int(x)-1, input().split()))[:-1]
    digraph[j]+=tmp
    graph[j]+=tmp
    for i in tmp:
        graph[i]+=[j]
in0=[]
out0=[]
for i in range(n):
    if not digraph[i]:
        out0.append(i)
    elif digraph[i]==graph[i]:
        in0.append(i)
strocon=[]
sum_of_strcon=0

for i in range(n):
    if i not in strocon:
        saikono_hamon(i, strocon)
        sum_of_strcon += 1
print(sum_of_strcon+sum(in0))
print(max(len(in0),len(out0)))