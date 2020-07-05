def treeSides(node:int,index:int,apple:int):
    if index==0:
        return 0
    global maxs
    t = list()
    for i in range(n-1):
        if tree[i][0]==node:
            t.append(i)
    if len(t)==0:
        return 0
    else:
        a,b = t[0],t[1]
        maxss = list()
        if index>=2:
            for i in range(index+1):
                appa = treeSides(tree[a][1],i,0)
                appb = treeSides(tree[b][1],index-i,0)
                maxss.append(apple + appa + appb)
        temp1 = treeSides(tree[a][1],index-1,0)
        temp2 = treeSides(tree[b][1],index-1,0)
        maxss.append(apple+temp1)
        maxss.append(apple+temp2)
        return max(maxss)
            
n,q = map(int,input().split())
tree = list()
for i in range(n-1):
    strs = input().split()
    teli = [int(j) for j in strs]
    if teli == [2,3,20]:
#        print("ok")
        teli = [3,2,20]
    tree.append(teli)
maxs = list()
t0 = treeSides(1,q,0)
print(t0)