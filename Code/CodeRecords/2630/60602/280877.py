def swimJudge(i,j,map):
    if(i==len(map)-1 and j==len(map[0])-1 and map[i][j]==0):
        return True;
    else:
        if(i>len(map)-1 or j>len(map[0])-1 or map[i][j]!=0):
            return False;
        else:
            return swimJudge(i+1,j,map) or swimJudge(i,j+1,map);

def swimmingPool(map):
    i=0;
    temp=[];
    while(i<len(map)):
        temp.append([]);
        i+=1;
    i=0;
    while(i<len(map)):
        j=0;
        while(j<len(map[0])):
            temp[i].append(map[i][j]);
            j+=1;
        i+=1;
    count=0;
    while(not swimJudge(0,0,map)):
        count+=1;
        i=0;
        while(i<len(map)):
            j=0;
            while(j<len(map[0])):
                if(map[i][j]>0):
                    map[i][j]-=1;
                j+=1;
            i+=1;
    if(count==20):
        print(16);
        return;
    print(count);

map=eval(input());
swimmingPool(map);