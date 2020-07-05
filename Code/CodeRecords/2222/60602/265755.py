def Function(stringLeft,stringRight):
    i=0;
    countA=0;
    countB=0;
    while(i<len(stringLeft)):
        if(stringLeft[i]=="x"):
            if(stringLeft[i-1]=="+"):
                countA+=1;
            elif(stringLeft[i-1]=="-"):
                countA-=1;
            else:
                countA+=int(stringLeft[i-2]+stringLeft[i-1]);
        i+=1;

    i=0;
    while(i<len(stringRight)):
        if(stringRight[i]=="x"):
            if(stringRight[i-1]=="+"):
                countB+=1;
            elif(stringRight[i-1]=="-"):
                countB-=1;
            else:
                countB+=int(stringRight[i-2]+stringRight[i-1]);
        i+=1;

    count=countA-countB;

    num=0;
    i=0;
    while(i<len(stringLeft)):
        try:
            if(stringLeft[i]>='0' and stringLeft[i]<='9' and stringLeft[i+1]!="x"):
                num-=int(stringLeft[i-1]+stringLeft[i]);
        except Exception as e:
            num-=int(stringLeft[i-1]+stringLeft[i]);
        i+=1;

    i=0;
    while(i<len(stringRight)):
        try:
            if(stringRight[i]>='0' and stringRight[i]<='9'and stringRight[i+1]!="x"):
                num+=int(stringRight[i-1]+stringRight[i]);
        except Exception as e:
            num += int(stringRight[i - 1] + stringRight[i]);
        i+=1;

    if(count==0 and num!=0):
        print("No solution");
        return ;
    elif(count==0 and num==0):
        print("Infinite solutions");
        return ;

    ans=num/count;
    print("x=",end="");
    print(ans);


string=str(input());
string=string.split("=");
if(string[0][0]!="-"):
    string[0]="+"+string[0];
if(string[1][0]!="-"):
    string[1]="+"+string[1];

Function(string[0],string[1]);

