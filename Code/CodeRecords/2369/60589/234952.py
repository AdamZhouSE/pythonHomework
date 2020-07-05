num=int(input())
nodes=[]
for i in range(num):
    nodes.append(input())
result=''


def makeTree(node):
    global result
    if node[0]!='*':
        result= result + node[0]
        for other in nodes:
            if other[0]==node[1]:
                makeTree(other)
                break
        for other in nodes:
            if other[0]==node[2]:
                makeTree(other)
                break
    return

makeTree(nodes[0])
print(result,end='')