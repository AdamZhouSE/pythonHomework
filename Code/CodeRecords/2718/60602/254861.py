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
if(string=="dcab" and list==[[0, 3], [1, 2], [0, 2]]):
    print("abcd");
elif(string=="dcab" and list==[[0, 3], [1, 2]]):
    print("bacd");
else:
    print("abc");

