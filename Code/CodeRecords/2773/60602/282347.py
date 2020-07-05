def maxMatrixLen(i,j,map,state,count):
    if(map[i][j]>state):
        count+=1;
        tempA=0;
        tempB=0;
        tempC=0;
        tempD=0;
        if(i+1<len(map)):
            tempA=maxMatrixLen(i+1,j,map,map[i][j],count);
        if(i-1>=0):
            tempB=maxMatrixLen(i-1,j,map,map[i][j],count);
        if(j+1<len(map[0])):
            tempC = maxMatrixLen(i, j+1, map,map[i][j], count);
        if(j-1>=0):
            tempD = maxMatrixLen(i , j-1, map,map[i][j], count);
        return max(tempA,tempB,tempC,tempD);
    return count;


list="";
while(True):
    temp=input();
    if(temp!=']'):
        list+=temp;
    else:
        list+=temp;
        break;

list=eval(list);
i=0;
ans=1;
while(i<len(list)):
    j=0;
    while(j<len(list[0])):
        count=maxMatrixLen(i,j,list,0,0);
        if(count>ans):
            ans=count;
        j+=1;
    i+=1;
print(ans);