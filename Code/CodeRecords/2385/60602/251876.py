def examBinary(string):
    i=1;
    while(i<len(string)):
        if((string[i]==string[i-1] and string[i]=="1")):
            return False;
        i+=1;
    return True;
def generateString(num,ans):
    i=0;
    temp=[];
    while(i<len(ans)):
        temp.append("0"+ans[i]);
        temp.append("1" + ans[i]);
        i+=1;
    num-=1;
    if(num==1):
        return temp;
    else:
        return generateString(num,temp);



def notFineBinary(num):
    i=0;
    string="";
    while(i<num):
        string+="0";
        i+=1;
    i=0;
    ans=generateString(num,["0","1"]);
    while(i<len(ans)):
        if(not examBinary(ans[i])):
            ans.remove(ans[i]);
            i-=1;
        i+=1;
    print(len(ans));





Total=int(input());
while(Total>0):
    temp=int(input());
    notFineBinary(temp);
    Total-=1;