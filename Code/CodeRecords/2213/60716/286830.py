def findpath(start:int,to:int,nodes:list()):
    nodes.append(start)
    if start==to:
        road.append(nodes)
        return
    for j in paths:
        if j[0]==start and j[1] not in nodes:
            temp = nodes.copy()
            findpath(j[1],to,temp)
    
n,m,q = map(int,input().split())
paths = list()
pathfororder = list()
for i in range(m):
    a,b = map(int,input().split())
    paths.append([a,b])
    pathfororder.append([b,a])
paths.extend(pathfororder)
#print(paths)
ans = ['No' for i in range(q)]
for i in range(q):
    l,r,s,t = map(int,input().split())
    road = list()
    findpath(s,t,[])
    print(road)
    for ele in road:
        print("check road:{}".format(ele))
        check = True
        order = list()
        order.append(0)
        for k in range(len(ele)-1):
            getIndex = paths.index([ele[k],ele[k+1]])
            order.append(getIndex)
            if getIndex>=m: getIndex-=m
            if not(getIndex+1>=l and getIndex+1<=r) or order[k+1]<=order[k]:
                print("{} denied".format([ele[k],ele[k+1]]))
                check = False
                break
        if check:
            ans[i]='Yes'
            break
for i in ans:
    print(i)