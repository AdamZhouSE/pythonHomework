graph=[]
for i in range(5):
    graph.append(input().split())
x=0
y=0
for line in range(5):
    for col in range(5):
        if graph[line][col]=='1':
            x=col+1
            y=line+1
            break
print(abs(x-3)+abs(y-3))