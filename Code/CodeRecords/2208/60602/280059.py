def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def leftLeastNum(list):
    i=0;
    ans=[];
    while(i<len(list)):
        j=i-1;
        while(j>=0):
            if(list[j]<list[i]):
                ans.append(list[j]);
                break;
            j-=1;
        else:
            ans.append(-1);
        i+=1;
    i=0;
    while(i<len(ans)):
        print(ans[i],end=" ");
        i+=1;
    print();
Total=int(input());
i=0;
while(i<Total):
    size=int(input());
    list=makeIntList(input().split(" "));
    leftLeastNum(list);
    i+=1;