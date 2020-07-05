def findRedundantConnection(edges):
    p = [[i] for i in range(len(edges) + 1)]
    for x, y in edges:
        if p[x] is not p[y]: 
            p[x].extend(p[y]) 
            for z in p[y]:
                p[z] = p[x] 
        else:
            return [x, y]



s=input()
s=s.replace('[', ' ')
s=s.replace(']', ' ')
s=s.replace(',', ' ')
l=s.split()
l= list(map(int, l))
edge=[]
for i in range(0, len(l), 2):
    edge.append([l[i], l[i+1]])
#print(edge)
print(findRedundantConnection(edge))