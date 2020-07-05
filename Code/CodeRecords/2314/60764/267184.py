n=int(input())
tree=[]
for i in range(n):
    tree.append(1+i)
print(" ".join(str(i) for i in tree),end=" ")