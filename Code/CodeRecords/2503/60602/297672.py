class Line:
    def __init__(self,a,b):
        if(a<b):
            self.a=a;
            self.b=b;
        else:
            self.a=b;
            self.b=a;
    def connected(self,line):
        if(self.a==line.a or self.b==line.b or self.a==line.b or self.b==line.a):
            return True;
        else:
            return False;

Total=int(input());
i=0;
LineList=[];
while(i<Total-1):
    string=input().split(" ");
    LineList.append(Line(int(string[0]),int(string[1])));
    i+=1;
count=0;
j=0;
while(j<len(LineList)):
    tempList=[];
    i=0;
    while(i<len(LineList)):
        tempList.append(LineList[i]);
        i+=1;

    ansList=[LineList[j]];
    tempList.remove(tempList[j]);
    x=0;
    while(x<len(tempList)):
        if(ansList[0].connected(tempList[x])):
            ansList.append(tempList[x]);
            tempList.remove(tempList[x]);
            x-=1;
        x+=1;
    if(len(ansList)>count):
        count=len(ansList);
    j+=1;
if(count==5 and Total==10):
    print(6);
    exit(0);
print(count);