def stringIndex(string):
    temp=sorted(string);
    i=0;
    tempList=[];
    ans=[];
    temps=[];
    while(i<len(string)):
        temps.append(string[i]);
        i+=1;
    string=temps;
    i=0;
    temp.append("-");
    while(i<len(string)):
        tempList.append(string.index(temp[i])+1);
        string[string.index(temp[i])]="-";
        if(temp[i]!=temp[i+1]):
            tempList.reverse();
            ans+=tempList;
            tempList=[];
        i+=1;
    i=0;
    while(i<len(ans)-1):
        print(ans[i],end=" ");
        i+=1;
    print(ans[len(ans)-1]);



string=input();
stringIndex(string);