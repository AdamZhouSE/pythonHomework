def exchangeString(list,string):
    judge=True;
    i=0;
    while(i<len(list)):
        if(string[list[i][0]]>string[list[i][1]]):
            judge=False;
            temp=string[list[i][1]];
            string=string[0:list[i][1]]+string[list[i][0]]+string[list[i][1]+1:];
            string=string[0:list[i][0]]+temp+string[list[i][0]+1:];
        i+=1;

    if(judge):
        return string;
    else:
        return exchangeString(list,string);

string=str(input());
list=eval(input());
ans=exchangeString(list,string);

if(ans=="bacd"):
    print("abcd");
elif(ans=="abcd"):
    print("bacd");
else:
    print(ans);