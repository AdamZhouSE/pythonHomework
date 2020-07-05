def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def numMovesStones(stones):
    length=len(stones);
    stones=sorted(stones);
    mx=stones[length-1]-stones[0]+1-length;
    mx-=min(stones[length-1]-stones[length-2]-1,stones[1]-stones[0]-1);
    mi=mx;
    i=0;
    cost=0;
    while(i<length):
        j=0;
        while(j+1<length and stones[j+1]-stones[i]+1<=length):
            j+=1;
        cost=length-(j-i+1);
        if(j-i+1==length-1 and stones[j]-stones[i]+1==length-1):
            cost=2;
        mi=min(mi,cost);
        i+=1;
    ans=[];
    ans.append(mi);
    ans.append(mx);
    print(ans);

numMovesStones(makeIntList(input().split(",")));