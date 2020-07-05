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
class inequality:
    def __init__(self,a,b,c):
        self.a=a;
        self.b=b;
        self.c=c;

    def exam(self,x):
        if(self.a*x+self.b>self.c):
            return True;
        else:
            return False;
Total=int(input());
i=0;
inequalityList=[];
while(i<Total):
    string=input().split(" ");
    if(string[0]=="Add"):
        string=string[1:];
        string=makeIntList(string);
        Inquality=inequality(string[0],string[1],string[2]);
        inequalityList.append(Inquality);
    elif(string[0]=="Del"):
        temp=int(string[1]);
        inequalityList[temp-1].c=10000000;
    elif(string[0]=="Query"):
        temp=int(string[1]);
        j=0;
        count=0;
        while(j<len(inequalityList)):
            if(inequalityList[j].exam(temp)):
                count+=1;
            j+=1;
        print(count);
    i+=1;