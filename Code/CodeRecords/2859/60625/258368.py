n=int(input())
graph=[]

for i in range(n):
    line = input()
    graph.append(line)

check=1
for l in range(n):
    if graph[l][l]!=graph[0][0] or graph[l][n-1-l]!=graph[0][0]:
        check=0
        break
    for c in range(n):
        if c!=l and c!= n-1-l:
            if graph[l][c]!=graph[0][1]:
                check=0
                break
    if check==0:
        break
if check==0 or graph[0][0]==graph[0][1]:
    print('NO')
else:
    print("YES")