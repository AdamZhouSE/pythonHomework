def abnormalStr(stringA,stringB):
    judge=True;
    i=0;
    ans="";
    while(i<len(stringA)):
        j=0;
        while(j<len(stringB)):
            if(stringA[i]==stringB[j]):
                judge=False;
            j+=1;
        if(judge):
            x=0;
            while(x<len(ans)):
                if(ans[x]==stringA[i]):
                    judge=False;
                x+=1;
            if(judge):
                ans+=stringA[i];
        i+=1;
        judge=True;
    return ans;

Total=int(input());
i=0;
while(i<Total):
    ans="";
    stringA=input();
    stringB=input();
    ans+=abnormalStr(stringA,stringB);
    ans+=abnormalStr(stringB,stringA);
    list=list(ans);
    list.sort();
    s = "".join(list)
    print(s);
    print();
    i+=1;