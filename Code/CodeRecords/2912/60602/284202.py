def LongestSubString(string):
    i=0;
    ans="";
    judge=True;
    while(i<len(string)):
        temp = "";
        j=i;
        while(j<len(string)):
            x=0;
            while(x<len(temp)):
                if(string[j]==temp[x]):
                    judge=False;
                x+=1;
            if(judge):
                temp+=string[j];
            else:
                if(len(temp)>len(ans)):
                    ans=temp;
                judge=True;
                break;
            judge=True;
            j+=1;
        i+=1;
    print(len(ans));

string=input();
LongestSubString(string);