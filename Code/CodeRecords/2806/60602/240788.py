def dafusMeat(listNeed, listPrice):
    storeNum = 0;
    i=0;
    cost=0;
    while(i<len(listNeed)):
        if(storeNum<listNeed[i]):
            cost+=(listNeed[i]-storeNum)*listPrice[i];
            j=i+1;
            while(j<len(listNeed)):
                if(listPrice[j]>=listPrice[i]):
                    storeNum+=listNeed[j];
                    cost+=listNeed[j]*listPrice[i];
                    j+=1;
                else:
                    break;
        else:
            storeNum-=listNeed[i];
        i+=1;
    print(cost);



Total=int(input());
i=0;
ans=[];
listNeed=[];
listPrice=[];
while(i<int(Total)):
    list=str(input());
    list=list.split(" ");
    listNeed.append(int(list[0]));
    listPrice.append(int(list[1]));
    i+=1;
dafusMeat(listNeed,listPrice);