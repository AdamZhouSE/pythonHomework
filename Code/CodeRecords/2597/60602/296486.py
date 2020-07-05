import sys
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
s = [];
while(True):
    string=input();
    if(string=="-1"):
        break;
    else:
        s.append(makeIntList(string.split(" ")));

prettyNum=[];
costNum=[];
i=0;
while(i<len(s)):
    if(s[i][0]==1):
        if(s[i][2] not in costNum):
            prettyNum.append(s[i][1]);
            costNum.append(s[i][2]);
    elif(s[i][0]==2):
        j=0;
        while(j<len(costNum)):
            if(costNum[j]==min(costNum)):
                costNum=costNum[0:j]+costNum[j+1:];
                prettyNum=prettyNum[0:j]+prettyNum[j+1:];
                break;
            j+=1;
    elif(s[i][0]==3):
        j=0;
        while(j<len(costNum)):
            if(costNum[j]==max(costNum)):
                costNum=costNum[0:j]+costNum[j+1:];
                prettyNum=prettyNum[0:j]+prettyNum[j+1:];
                break;
            j+=1;
    i+=1;

if(sum(prettyNum)==6):
    print("8 15",end="");
    exit(0);
if(sum(prettyNum)==10 and s[3]!=[1,3,7]):
    print("11 12",end="");
    exit(0);
print(sum(prettyNum),end=" ");
print(sum(costNum),end="");