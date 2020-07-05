def missingString(s1,s2):
    i=0;
    judge=False;
    ans=[];
    count=0;
    while(i<len(s2)):
        j=0;
        while(j<len(s1)):
            if(s2[i+j]==s1[j] or s1[j]=='*' or s2[i+j]=='*'):
                if(j==len(s1)-1):
                    judge=True;
            else:
                break;
            j+=1;
        if(judge):
            count+=1;
            ans.append(i+1);
        judge=False;
        i+=1;
    if(count>0):
        print(count);
        i=0;
        while(i<len(ans)):
            print(ans[i],end=" ");
            i+=1;
        print();
        
    else:
        print(count);


size=input().split(" ");

s1=input();
s2=input();
missingString(s1,s2);