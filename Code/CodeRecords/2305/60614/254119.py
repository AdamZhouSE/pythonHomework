class vertice():
    def __init__(self,point):
        self.point=point
        self.edge=[]
    def add(self,edge):
        self.edge.append(edge)
fInput=[int(x) for x in input().split()]
points=fInput[0]
colors=fInput[1]
numOfAlice=int(input())
alice=[]
for i in range(numOfAlice):
    alice.append(vertice([int(x) for x in input().split()]))
numOfShinobu=int(input())
shinobu=[]
for i in range(numOfShinobu):
    shinobu.append(vertice([int(x) for x in input().split()]))
edges=[]
for i in range(len(alice)):
    for j in range(len(shinobu)):
        if alice[i].point[0] == shinobu[j].point[0] or alice[i].point[1] == shinobu[j].point[1]:
            edges.append([i,j])
            alice[i].add([i,j])
            shinobu[j].add([i,j])
matches=[-1]*len(shinobu)
def dfs(origin,ban):
    if origin == ban:
        return False
    for j in alice[origin].edge:
        if not visited[j[1]]:
            visited[j[1]]=True
            if matches[j[1]]==-1 or dfs(matches[j[1]],ban):
                matches[j[1]]=origin
                return True
    return False
for i in range(len(alice)):
    visited = [False] * len(shinobu)
    dfs(i,-2)
while -1 in matches:
    matches.remove(-1)
former=len(matches)
for i in range(len(alice)):
    matches = [-1] * len(shinobu)
    for j in range(len(alice)):
        visited = [False] * len(shinobu)
        dfs(j,i)
    while -1 in matches:
        matches.remove(-1)
    if len(matches)==former:
        print(0)
    else:
        print(1)