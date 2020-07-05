def reShapeString(string):
    ans=string[0];
    i=1;
    while(i<len(string)):
        if(string[i]!=ans[len(ans)-1]):
            ans+=string[i];
        else:
            j=i+1;
            while(j<=len(string)):
                try:
                    if(string[j]!=ans[len(ans)-1]):
                        ans+=string[j];
                        string=string[0:j]+string[j+1:];
                        i-=1;
                        break;
                    j+=1;
                except Exception as e:
                    print("");
                    return;
        i+=1;
    print(ans);

string=input();
reShapeString(string);