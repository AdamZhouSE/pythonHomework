string =input()
circle=0
for c in string:
    if c.isdigit():
        circle=circle+1
    elif c == ']':
        break
list_circle = [[0 for i in range(circle)] for j in range(circle)]

i=0
j=0
while i<circle:
    for c in string:
        if c.isdigit():
            list_circle[i][j]=c
            j=j+1
        if j==3:
            j=0
            i=i+1
res=0
hasVisited=[0 for i in range(circle)]
def dfs(list_circle,i,hasVisited):
    hasVisited[i]=1
    for k in range(circle):
        if list_circle[i][k]=='1' and hasVisited[k] == 0:
            dfs(list_circle,k,hasVisited)

for i in range(circle):
    if hasVisited[i]!=1:
        dfs(list_circle,i,hasVisited)
        res=res+1
print(res)