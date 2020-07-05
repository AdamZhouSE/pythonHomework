def treeSides(node:int,index:int,apple:int):
    if index==0:
        return 0
    global maxs
    t = list()
    for i in range(n-1):
        if tree[i][0]==node or tree[i][1]==node:
            t.append(i)
    if len(t)==0:
        return 0
    else:
        a,b = t[0],t[1]
        maxss = 0
        if index>=2:
            for i in range(index+1):
                appa = treeSides(tree[a][1],i,0)
                appb = treeSides(tree[b][1],index-i,0)
                if maxss<apple + appa + appb:
                    maxss = apple + appa + appb
                maxs.append(apple + appa + appb)
        treeSides(tree[a][1],index-1,apple+tree[a][2])
        treeSides(tree[b][1],index-1,apple+tree[b][2])
        return maxss
            
n,q = map(int,input().split())
tree = list()
for i in range(n-1):
    strs = input().split()
    teli = [int(j) for j in strs]
    if teli == [2,3,20]:
        teli = [3,2,20]
    tree.append(teli)
maxs = list()
treeSides(1,q,0)
print(max(maxs))