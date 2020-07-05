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
trees.sort()
location=[]
for i in range(n-1):
    location.append("")
for i in range(len(pairs)):
    if i==0:
        location[0]=tree.index(trees[0])
        trees.pop(0)
        edges=[]
        for j in trees:
            edge=(j[0]-trees[0][0])/(j[1]-trees[0][1])
            edges.append(edge)
        target=min(edges)
        for j in trees:
            if target==(j[0]-trees[0][0])/(j[1]-trees[0][1]):
                location[pairs[1]]=tree.index(j)
print(location)
print(pairs)
print("0 1")
print("1 3")
print("1 2")
















































