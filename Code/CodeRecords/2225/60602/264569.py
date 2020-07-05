def reverseAll(LanternList):
    i=0;
    while(i<len(LanternList)):
        LanternList[i]=not LanternList[i];
        i+=1;
    return LanternList;

def reverseOdd(LanternList):
    i=0;
    while(i<len(LanternList)):
        if((i+1)%2==1):
            LanternList[i]=not LanternList[i];
        i+=1;
    return LanternList;

def reverseEven(LanternList):
    i=0;
    while(i<len(LanternList)):
        if((i+1)%2==0):
            LanternList[i]=not LanternList[i];
        i+=1;
    return LanternList;

def reverseThr(LanternList):
    i=0;
    while(i<len(LanternList)):
        if((i)%3==0):
            LanternList[i]=not LanternList[i];
        i+=1;
    return LanternList;

def checkList(LanternList,ans):
    i=0;
    judge=True;
    while(i<len(ans)):
        if(ans[i]==LanternList):
            judge=False;
            break;
        i+=1;
    return judge;

def copyList(LanternList):
    i=0;
    temp=[];
    while(i<len(LanternList)):
        temp.append(LanternList[i]);
        i+=1;
    return temp;

def roomLantern(LanternList,i,m,ans):
    while(i<m):
        temp=copyList(LanternList);
        temp=reverseAll(temp);
        if(checkList(temp,ans)):
            ans.append(temp);
        ans=roomLantern(temp,i+1,m,ans);

        temp = copyList(LanternList);
        temp=reverseOdd(temp);
        if(checkList(temp,ans)):
            ans.append(temp);
        ans=roomLantern(temp,i+1,m,ans);

        temp = copyList(LanternList);
        temp=reverseEven(temp);
        if(checkList(temp,ans)):
            ans.append(temp);
        ans=roomLantern(temp,i+1,m,ans);

        temp = copyList(LanternList);
        temp=reverseThr(temp);
        if(checkList(temp,ans)):
            ans.append(temp);
        ans=roomLantern(temp,i+1,m,ans);
        i+=1;
    else:
        return ans;

n=int(input());
m=int(input());

LanternList=[];

i=0;
while(i<n):
    LanternList.append(True);
    i+=1;
print(len(roomLantern(LanternList,0,m,[])));