def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def candyForChildren(list,m):
    list=makeIntList(list);
    counter=len(list);
    i=0;
    while(True):
        while(i<len(list)):
            if(list[i]>0):
                list[i]-=m;
                if(list[i]<=0):
                    counter-=1;
                    if (counter == 0):
                        print(i + 1);
                        return ;
            i+=1;
        i=0;




Total=str(input());
Total=Total.split(" ");
list=str(input());
list=list.split(" ");
candyForChildren(list,int(Total[1]));