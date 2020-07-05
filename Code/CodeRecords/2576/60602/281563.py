def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;

def reverseMostList(list,Target):
    SUM=0;
    value=0;
    ans=0;
    delta=100000;
    while(value<=max(list)):
        i=0;
        temp=[];
        while(i<len(list)):
            temp.append(list[i]);
            i+=1;
        j=0;
        while(j<len(list)):
            if(list[j]>value):
                temp[j]=value;
            j+=1;
        SUM=sum(temp);
        if(abs(Target-SUM)<delta):
            delta=abs(Target-SUM);
            ans=value;
        value+=1;
    print(ans);

list=makeIntList(input().split(","));
Target=int(input());
reverseMostList(list,Target);