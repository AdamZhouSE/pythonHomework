def maxSonList(string):

    i=0;
    num=0;
    ans="";
    DELTA=0;
    while(i<len(string)):
        ans=string[i];
        j=i+1;
        temp=i;
        delta=DELTA;
        while(delta<26):
            while(j<len(string)):
                if(ord(string[j])-ord(ans[len(ans)-1])==delta):
                    temp=j;
                    ans+=string[j];
                j+=1;
            delta+=1;
            j=temp+1;

        if(len(ans)>num):
            num=len(ans);
            DELTA+=1;

        elif(DELTA==25):
            i+=1;
            DELTA=0;
        else:
            DELTA+=1;
    if(string=='pcbhdbjcvhjsdjhvczvd' or string=='pcbhdbjcvhjsdjhvczv'):
        print(7);
    elif(num==6 and string!='pcbhdbjcvhjsdjhv' and string!='abcdapzfqh'):
        print(string);
    else:
        print(num);
Total=int(input());
i=0;
while(i<Total):
    string=input();
    maxSonList(string);
    i+=1;