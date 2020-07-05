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
Total=int(input());
list=makeIntList(input().split(" "));
size=int(input());
i=0;
while(i<size):
    temp=makeIntList(input().split(" "));
    tempList=list[temp[0]-1:temp[1]];
    j=min(tempList);
    count=0;
    while(j<=max(tempList)):
        if(tempList.count(j)>=1):
            count+=1;
        j+=1;
    print(count);
    i+=1;