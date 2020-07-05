from itertools import combinations
n=int(input())
pairs=[]
for i in range(n-1):
    x=input().split(" ")
    pairs.append([int(x[1]),int(x[0])])
tree=[]
for i in range(n):
    x=input().split(" ")
    tree.append([int(x[0]),int(x[1])])
trees=tree.copy()
location=[]
for i in range(n):
    location.append("")
location[0]=tree.index(trees[0])
trees.pop(0)
for i in range(len(pairs)):
    x=pairs[i]
    start=x[0]
    end=x[1]
    edges=[]
    for j in trees:
        if j[1]-tree[location[start]][1]==0:
            edges.append("")
        else:
            edges.append(abs((j[0]-tree[location[start]][0])/(j[1]-tree[location[start]][1])))
    target=""
    for j in edges:
        if j!="":
            target=j
            break
    if target!="":
        for j in edges:
            if j!="":
                if j<target:
                    target=j
    location[end]=tree.index(trees[edges.index(target)])
    trees.pop(edges.index(target))
for i in pairs:
    print(str(location[i[0]])+" "+str(location[i[1]]))
















































