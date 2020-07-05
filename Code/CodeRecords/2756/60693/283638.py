def findShortColorPath(n:int,red_edges:[[int]],blue_edges:[[int]]):
    red_path=[set() for _ in range(n)]
    blue_path=[set() for _ in range(n)]
    dis=[[None,None] for _ in range(n)]  # dis[i][0] means the shortest path 0-i start by res,dis[i][1] means the shortest path 0-i start by blue
    dis[0]=[0,0]
    for x,y in red_edges:
        red_path[x].add(y)
    for x,y in blue_edges:
        blue_path[x].add(y)

    step,nr,nb=0,[0],[0]
    while len(nr) or len(nb):
        newr,newb=[],[]
        step+=1
        if len(nb):
            for p in nb:
                for np in red_path[p]:
                    if dis[np][0] is None:
                        dis[np][0]=step
                        newr.append(np)
        if len(nr):
            for p in nr:
                for np in blue_path[p]:
                    if dis[np][1] is None:
                        dis[np][1]=step
                        newb.append(np)

        nr,nb=newr,newb

    res=[]
    for i in range(n):
        if dis[i][0] is None and dis[i][1] is None:
            res.append(-1)
        elif dis[i][0] is not None and dis[i][1] is not None:
            res.append(min(dis[i][0],dis[i][1]))
        elif dis[i][0] is None:
            res.append(dis[i][1])
        else:
            res.append(dis[i][0])

    return res


n=int(input())
red_edges=eval(input())
blue_edges=eval(input())
print(findShortColorPath(n,red_edges,blue_edges))