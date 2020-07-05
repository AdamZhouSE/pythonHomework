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
times=int(input());
strnum="["
for i in range(times):
    strnum+="["+input()+"],";
strnum+="]"
numslist=eval(strnum);
finx=len(numslist)-1
finy=len(numslist[0])-1
healthypoints=[];
dfs(0,0,finx,finy,0,0);
healthypoints.sort(reverse=True)
print(1-healthypoints[0])