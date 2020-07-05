def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def RightBiggerNum(list):
    i=0;
    ans=[];
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            if(list[j]>=list[i]):
                ans.append(list[j]);
                break;
            j+=1;
        else:
            ans.append(-1);
        i+=1;
    i=0;
    while(i<len(ans)-1):
        print(ans[i],end=" ");
        i+=1;
    print(ans[len(ans)-1]);
    
Total=int(input());
i=0;
while(i<Total):
    S=input();
    list=makeIntList(input().split(" "));
    RightBiggerNum(list);
    i+=1;