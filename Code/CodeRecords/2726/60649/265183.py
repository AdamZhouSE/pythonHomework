import math
tree=input()[1:-1:]
tree=tree.split(",")
for i in range(len(tree)):
    if (2*i+1==len(tree)-1and tree[2*i+1]=='null') or 2*+1>=len(tree) or (tree[2*i+1]=='null' and tree[2*i+2]=='null'):
        print(int(math.log(i+1,2))+1)
        break
else:
    print(int(math.log(i),2)+1)