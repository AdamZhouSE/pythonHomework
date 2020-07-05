from itertools import combinations
n=int(input())
pairs=[]
for i in range(n-1):
    x=input().split(" ")
    pairs.append([int(x[0]),int(x[1])])
trees=[]
for i in range(n):
    x=input().split(" ")
    trees.append([int(x[0]),int(x[1])])
lists=[]
for i in range(n):
    lists.append(i)
target=[]
for a in list(combinations(lists,2)):
    target.append(list(a))
targets=[]
for a in list(combinations(target,n-1)):
     targets.append(list(a))
print(targets)
print(pairs)
print(trees)
















































