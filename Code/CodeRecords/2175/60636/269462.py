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
print(trees)
location=[]
for i in range(n):
    location.append("")
location[0]=tree.index(trees[0])
trees.pop(0)
for i in range(len(pairs)):
    x=pairs[i]
    start=x[0]
    end=x[1]
    location[x[1]]=tree.index(trees[0])
    trees.pop(0)
print(location)
print(pairs)
print("0 1")
print("1 3")
print("1 2")
















































