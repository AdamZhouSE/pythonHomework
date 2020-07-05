n=int(input())
tree=eval(input())
matrix=[[0 for i in range(n)]for i in range(n)]
for i in tree:
    matrix[i[0]][i[1]]=1
    matrix[i[1]][i[0]]=1

ll=[]
def deep(current,visited):
    for i in range(n):
        if(matrix[current][i]==1 and i not in visited):
            visited.append(i)
            ll.append(len(visited))
            deep(i,visited)
            visited.remove(i)

out=[0 for i in range(n)]
for i in range(n):
    count=0
    visited=[i]
    ll=[]
    deep(i,visited)
    out[i]=max(ll)
min_=min(out)
result=[]
for i in range(n):
    if out[i]==min_:
        result.append(i)
print(result)