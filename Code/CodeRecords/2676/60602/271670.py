def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def maxKsizeList(list,K):
    i=0;
    ans=0;
    while(i+K<=len(list)):
        j=0;
        count=0;
        while(j<K):
            count+=list[i+j];
            j+=1;
        if(count>ans):
            ans=count;
        i+=1;
    print(ans);
Total=int(input());
i=0;
while(i<Total):
    NK=input().split(" ");
    list=makeIntList(input().split(" "));
    maxKsizeList(list,int(NK[1]));
    i+=1;