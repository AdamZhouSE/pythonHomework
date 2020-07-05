n = int(input())
nodes = []
for i in range(0,n-1):
    nodes.append(input().split(' '))
for i in range(0,n-1):
    nodes[i][0]=int(nodes[i][0])
    nodes[i][1]=int(nodes[i][1])
    nodes.append([nodes[i][1],nodes[i][0]])


def dfs(a,b):
    max1  =0
    for i in range(0,len(nodes)):
        if nodes[i][0]==b and nodes[i][1]!=a:
            temp = dfs(nodes[i][0],nodes[i][1])+1
            max1 = max(max1,temp)
    if max1 ==0:
        return 1
    else:
        return max1

result =0
for i in range(0,len(nodes)):
    result = max(result,dfs(nodes[i][0],nodes[i][1]))

print(result)