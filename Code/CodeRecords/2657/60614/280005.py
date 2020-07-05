init=[int(x) for x in input().split()]
nodes=[True]*init[0]
edges=[]
for i in range(init[0]-1):
    edges.append([int(x) for x in input().split()])
for i in edges:
    nodes[i[1]-1]=False
for i in range(init[1]):
    operation=input().split()
    if operation[0]=='Q':
        key=int(operation[1])
        if nodes[key-1]:
            print(key)
        else:
            j=0
            while j<len(edges):
                if edges[j][1]==key:
                    if nodes[edges[j][0]-1]:
                        print(edges[j][0])
                        break
                    else:
                        key=edges[j][0]
                        j=-1
                j+=1
    else:
        nodes[int(operation[1])-1]=True