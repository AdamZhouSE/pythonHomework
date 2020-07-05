def dfs(x:int,y:int,fx:int,fy:int,hpointmaxnegv:int,hpoint:int):
    if(x==fx and y==fy):
        hpoint += numslist[x][y];
        if (hpoint < hpointmaxnegv):
            hpointmaxnegv = hpoint;
        healthypoints.append(hpointmaxnegv);
    hpoint+=numslist[x][y];
    if(hpoint<hpointmaxnegv):
        hpointmaxnegv=hpoint;
    if(x+1<=fx):
        dfs(x+1,y,fx,fy,hpointmaxnegv,hpoint)
    if(y+1<=fy):
        dfs(x,y+1,fx,fy,hpointmaxnegv,hpoint)
    #没有符合条件的自然return！！！
numslist=[[-2,-3,3],[-5,-10,1],[10,30,-5]];
healthypoints=[];
dfs(0,0,2,2,0,0);
healthypoints.sort(reverse=True)
print(1-healthypoints[0])