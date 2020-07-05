def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def longestArray(list):
    list=makeIntList(list);
    ans=1;
    count=1;
    i=1;
    while(i<len(list)):
        if(list[i]>list[i-1]):
            count+=1;
        else:
            count=1;
        if (count > ans):
            ans = count;
        i+=1;
    print(ans);

Total=int(input());
list=str(input());
list=list.split(" ");
longestArray(list);