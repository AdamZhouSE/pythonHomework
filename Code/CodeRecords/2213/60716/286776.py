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
for i in range(m):
    a,b = map(int,input().split())
    paths.append([a,b])
#print(paths)
ans = ['NO' for i in range(q)]
for i in range(q):
    l,r,s,t = map(int,input().split())
    road = list()
    findpath(s,t,[])
    print(road)
    for ele in road:
        check = True
        for k in range(len(ele)-1):
            if not(paths.index([ele[k],ele[k+1]])+1>=l and paths.index([ele[k],ele[k+1]])+1<=r):
                check = False
                break
        if check:
            ans[i]='Yes'
            break
for i in ans:
    print(i)