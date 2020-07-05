def treeSides(node:int,index:int,apple:int):
    global maxs
    if index==0:
        if apple>maxs : maxs = apple
        return
    for temp in tree:
        if temp[0]==node:
            treeSides(temp[1],index-1,apple+temp[2])
n,q = map(int,input().split())
tree = list()
for i in range(n-1):
    strs = input().split()
    teli = [int(j) for j in strs]
    tree.append(teli)
maxs = 0
treeSides(1,q,0)
print(maxs)
if maxs==0:
    print(tree)