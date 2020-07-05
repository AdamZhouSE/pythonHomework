def leaststr(str1,str2):
    i=0;
    ans="";
    count=0;
    x=0;
    judge=True;
    while(x<len(str2)):
        ans+=str2[x];
        x+=1;
        judge=True;
    while(i<len(str1)):
        j=0;
        while(j<len(str2)):
            if(str2[j]==str1[i]):
                judge=False;
            j+=1;
        if(judge):
            ans+=str1[i];
        i+=1;
    print(len(ans));
Total=int(input());
i=0;
while(i<Total):
    list=input().split(" ");
    str1=list[0];
    str2=list[1];
    leaststr(str1,str2);
    i+=1;