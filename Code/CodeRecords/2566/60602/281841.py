def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def UWgame(HP,i,j,map):
    if(i==len(map)-1 and j==len(map[0])-1):
        if(HP+map[i][j]>0):
            return True;
        else:
            return False;
    else:
        if(i>len(map)-1 or j>len(map[0])-1):
            return False;
        else:
            if (HP + map[i][j] > 0):
                return UWgame(HP + map[i][j],i+1,j,map) or UWgame(HP + map[i][j],i,j+1,map);
            else:
                return False;

Total=int(input());
i=0;
ans=[];
while(i<Total):
    temp=makeIntList(input().split(","));
    ans.append(temp);
    i+=1;

j=1;
while(not UWgame(j,0,0,ans)):
    j+=1;
print(j);