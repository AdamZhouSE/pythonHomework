def IslandNum(i,j,map):
    if(i<len(map) and j<len(map[0]) and map[i][j]==1):
        map[i][j]=0;
        map=IslandNum(i+1,j,map);
        map=IslandNum(i,j+1,map);
        return map;
    else:
        return map;

def examMap(map):
    judge=False;
    i=0;
    while(i<len(map)):
        j=0;
        while(j<len(map[0])):
            if(map[i][j]!=0):
                judge=True;
            j+=1;
        i+=1;
    return judge;


temp=4;
s = [];
i=0;
while(i<temp):
    s.append(input());
    i+=1;


i=0;
ans=[];
while(i<len(s)):
    j=0;
    ans.append([]);
    while(j<len(s[i])):
        ans[i].append(int(s[i][j]));
        j+=1;
    i+=1;

i=0;
map=ans;
count=1;
while(i<len(map)):
    j=0;
    while(j<len(map)):
        if(map[i][j]==1):
            map=IslandNum(i,j,map);
            if(examMap(map)):
                count+=1;
            else:
                break;
        j+=1;
    i+=1;
print(count);