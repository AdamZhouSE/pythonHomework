def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def kaisaGame(list):
    list=makeIntList(list);
    sum=0;
    cost=list[0];
    i=1;
    while(i<len(list)):
        if(sum+list[i-1]-list[i]<0):
            cost=cost-(sum+list[i-1]-list[i]);
            list[i-1]+=-(sum+list[i-1]-list[i]);
            sum = 0;

        else:
            sum=sum+list[i-1]-list[i];
        i+=1;
    print(cost);




Total=int(input());
list=str(input());
list=list.split(" ");
kaisaGame(list);