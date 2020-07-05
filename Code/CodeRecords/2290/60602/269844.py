def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def nextSmaller(list):
    i=0;
    ans=[];
    while(i<len(list)-1):
        if(list[i]>list[i+1]):
            ans.append(list[i+1]);
        else:
            ans.append(-1);
        i+=1;
    i=0;
    ans.append(-1);
    while(i<len(ans)-1):
        print(ans[i],end=" ");
        i+=1;
    print(ans[len(ans)-1],end=" ");
    print();

Total=int(input());
i=0;

while(i<Total):
    length=int(input());
    temp=makeIntList(input().split(" "));
    nextSmaller(temp);
    i+=1;