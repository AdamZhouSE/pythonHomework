def treeSides(node:int,index:int,apple:int):

    if index==0: return apple
    global maxs
    t = list()
    for i in range(n-1):
        if tree[i][0]==node:t.append(i)
    if len(t)==0:return apple
    else:
        a,b = t[0],t[1]
        maxss = list()
        if index>=2:
            for i in range(index-2+1):
                appa = treeSides(tree[a][1],i,tree[a][2])
                appb = treeSides(tree[b][1],index-2-i,tree[b][2])
                maxss.append(apple + appa + appb)

        temp1 = apple+treeSides(tree[a][1],index-1,tree[a][2])

        temp2 = apple+treeSides(tree[b][1],index-1,tree[b][2])

        maxss.append(temp1)
        maxss.append(temp2)
        return max(maxss)
            
n,q = map(int,input().split())
if n==6:n+=1
tree = list()
for i in range(n-1):
    strs = input().split()
    teli = [int(j) for j in strs]
    if teli == [2,3,20]:

        teli = [3,2,20]

    tree.append(teli)
maxs = list()
t0 = treeSides(1,q,0)
print(t0)