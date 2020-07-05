import re
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
edges=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        edges.append(new)
        a=0
        new=[]
parents = list(range(len(edges) + 1))
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]
for edge in edges:
    i, j = find(edge[0]), find(edge[1])
    if i == j:
        print (edge)
    else:
        parents[i] = j