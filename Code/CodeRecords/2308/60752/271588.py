
def findindex(tree,name):
    for t in range(len(tree)):

        if str(tree[t][0])==str(name):return t
    return -1

def loop(line,tree,index):
    if tree[index][1]!=0:loop(line,tree,findindex(tree,tree[index][1]))
    line.append(tree[index][0])
    if tree[index][2] != 0: loop(line, tree, findindex(tree,tree[index][2]))

tree=[]
line1=input().split()
root=line1[1]
for node in range(int(line1[0])):
    tree.append(list(map(int,input().split())))
line=[]
loop(line,tree,findindex(tree,root))
find =int(input())
i=0
for i in range(len(line)):
    if line[i]==find:break
if i==len(line)-1:
    print(0)
else:
    print(line[i+1])


