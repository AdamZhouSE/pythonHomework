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
class cowSaver:
    def __init__(self,i,j):
        self.i=i;
        self.j=j;

def examCowSaver(list,Saver):
    count=0;
    x=Saver.i-1;
    while(x<Saver.j-1):
        list[x]-=1;
        x+=1;
    y=0;
    while(y<len(list)):
        if(list[y]!=0):
            count+=1;
        y+=1;
    return count;

size=0;
list=[];
while(size<10000):
    list.append(0);
    size+=1;

Total=int(input());
x=0;
saverList=[];
while(x<Total):
    temp=makeIntList(input().split(" "));
    i=temp[0];
    j=temp[1];
    saverList.append(cowSaver(i,j));
    y=i-1;
    while(y<j-1):
        list[y]+=1;
        y+=1;
    x+=1;
x=0;
ans=0;
while(x<len(saverList)):
    z=0;
    tempList=[];
    while(z<len(list)):
        tempList.append(list[z]);
        z+=1;
    tempNum=examCowSaver(tempList,saverList[x]);
    if(tempNum>ans):
        ans=tempNum;
    x+=1;
print(ans,end="");
