n=int(input())
nodes=[]
for i in range(n):
    nodes.append(input())
result=""

def makeTree(node):
    global result
    if node[0]!="*":
        result+=node[0]
        for i in range(len(nodes)):
            if nodes[i][0]==node[1]:
                makeTree(nodes[i])
                break
        for i in range(len(nodes)):
            if nodes[i][0]==node[2]:
                makeTree(nodes[i])
                break
    return 
makeTree(nodes[0])
print(result,end="")