def makeIntList(list):
    count = 0;
    ans=[];
    while (count < len(list)):
        try:
            ans.append(int(list[count]));
        except Exception as e:
            count+=1;
            continue;
        count += 1;
    return ans;
Total=makeIntList(input().split(" "));
moveStep=Total[0];
K=Total[1];
i=0;
Length=[];
Direction=[];
while(i<moveStep):
    string=input().split(" ");
    Length.append(int(string[0]));
    Direction.append(string[1]);
    i+=1;

list=[];
i=0;
while(i<2000000):
    list.append(0);
    i+=1;
j=1000000;
i=0;
while(i<len(Direction)):
    if(i>=1):
        if(Direction[i-1]=="R" and Direction[i]=="L"):
            j-=1;
        if(Direction[i-1]=="L" and Direction[i]=="R"):
            j+=1;
    if(Direction[i]=="R"):
        x=0;
        while(x<Length[i]):
            list[j+x]+=1;
            x+=1;
        j=j+x;
    else:
        x=0;
        while(x<Length[i]):
            list[j-x]+=1;
            x+=1;
        j=j-x;
    i+=1;

count=0;
i=0;
while(i<len(list)):
    if(list[i]>=K):
        count+=1;
    i+=1;

print(count,end="");