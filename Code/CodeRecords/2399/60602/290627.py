import math
def makeIntList(list):
    count = 0;
    ans=[];
    while (count < len(list)):
        if(list[count]>='0' and list[count]<='9'):
            ans.append(int(list[count]));
        count += 1;
    return ans;
def GoboSort(list,l,r,m):
    while(m>0):
        countList=[];
        i=l;
        while(i<=r):
            countList.append(list.count(i));
            i+=1;
        i=l;
        while(i<=r):
            if(list.count(i)==min(countList)):
                list.append(i);
                break;
            i+=1;
        m-=1;

    allPoss=math.factorial(len(list));
    countList=[];
    while(list!=[]):
        countList.append(list.count(list[0]));
        temp=list[0];
        t=0;
        while(t<len(list)):
            if(list[t]==temp):
                list.remove(list[t]);
                t-=1;
            t+=1;
    i=0;
    while(i<len(countList)):
        allPoss/=math.factorial(countList[i]);
        i+=1;
    print(int(allPoss)%998244353);

Total=int(input());
i=0;
while(i<Total):
    size=makeIntList(input().split(" "));
    m=size[1];
    l=size[2];
    r=size[3];
    list=makeIntList(input().split(" "));
    GoboSort(list,l,r,m);
    i+=1;