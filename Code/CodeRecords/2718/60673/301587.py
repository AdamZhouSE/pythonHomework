import collections

string=input()
inp=input()
pairs=inp[2:-2].split("],[")
for i in range(len(pairs)):
    pairs[i]=pairs[i].split(",")
for i in range(len(pairs)):
    for j in range(2):
        pairs[i][j]=int(pairs[i][j])
parent=[i for i in range(len(string))]

def find(x):
    if(parent[x]==x):return x
    else:
        return find(parent[x])

def union(x,y):
    x_root=find(x)
    y_root=find(y)
    if(x_root!=y_root):
        parent[x_root]=y_root

for i in pairs:
    union(i[0],i[1])
ans=list(string)
de=collections.defaultdict(list)
for i,j in enumerate(map(find,parent)):
    de[j].append(i)

for q in de.values():
    t=sorted(ans[i] for i in q)
    for i,c in zip(sorted(q),t):
        ans[i]=c
print("".join(ans))



