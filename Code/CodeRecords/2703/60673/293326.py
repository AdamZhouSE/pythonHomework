
def findfriend(relation,l):
    visited,ans=set(),0

    def dfs(i):
        for j in range(l):
            if relation[i][j] and j not in visited:
                visited.add(j)
                dfs(j)

    for i in range(l):
        if i not in visited:
            dfs(i)
            ans+=1
    return ans

n1=input()
n=n1[1:-1].split("], [")
relation=[]
temp=[]
l=len(n)
for i in range(l):
    temp=n[i][1:].split(",")
    relation.append(temp)
for i in range(l):
    for j in range(i,l):
        if(relation[i][j]==1):
            relation[j][i]=1

print(findfriend(relation,l))
